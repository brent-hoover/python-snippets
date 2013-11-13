from django.views.generic import TemplateView

from celery.result import AsyncResult
from celery.registry import tasks

class BaseResponseView(TemplateView):
    result = None
    
    def get_context_data(self, **kwargs):
        context = super(BaseResponseView, self).get_context_data(**kwargs)
        context['result'] = self.result
        return context

class WaitForResponseView(BaseResponseView):
    template_name = 'tasks/wait_for_response.html'

class TaskFailedResponseView(BaseResponseView):
    template_name = 'tasks/task_failed_response.html'

class TaskViewMixin(object):
    session_key = 'asynctask_token'
    wait_for_response_view = WaitForResponseView
    task_failed_response_view = TaskFailedResponseView
    
    task_name = None #please define this
    
    def get_task_kwargs(self):
        return {}
    
    def schedule_task(self):
        task = tasks[self.task_name]
        kwargs = self.get_task_kwargs()
        result = task.apply_async(kwargs=kwargs)
        self.set_task_token(result.task_id)
        return result
        
    def get_task_token(self):
        return self.request.session.get(self.session_key, None)
    
    def set_task_token(self, task_id):
        self.request.session[self.session_key] = task_id
    
    def clear_task_token(self):
        del self.request.session[self.session_key]
    
    def task_status(self):
        task_id = self.get_task_token()
        if task_id is None:
            return None
        return AsyncResult(task_id)
    
    def get(self, request, **kwargs):
        result = self.task_status()
        if result is None or request.REQUEST.get('recreate', False):
            result = self.schedule_task()
        if result.failed():
            self.clear_task_token()
            return self.render_task_failed_response(result)
        elif result.successful():
            self.clear_task_token()
            return self.render_task_success_response(result)
        else:
            return self.render_wait_for_response(result)
    
    def render_wait_for_response(self, result):
        return self.wait_for_response_view(result=result).dispatch(self.request)
    
    def render_task_failed_response(self, result):
        return self.task_failed_response_view(result=result).dispatch(self.request)
    
    def render_task_success_response(self, result):
        return self.render_to_response({'result':result})

class ExampleTaskView(TaskViewMixin, TemplateView):
    template_name = 'tasks/task_success.html'
    task_name = 'celery.ping'

example_view = ExampleTaskView.as_view()
