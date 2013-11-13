class MyView(View):
    """Displays the details of a BlogPost"""

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "blog/blogpost_detail.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "blogpost": self.get_object(),
        }

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(BlogPost, pk=self.kwargs.get("pk"))