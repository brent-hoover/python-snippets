THIS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.join(THIS_DIR, 'relative/path/to/your/project/')
sys.path.append(PROJECT_DIR)

import inspect
import settings
from django.core.management import setup_environ
from django.utils.html import strip_tags
from django.utils,encoding import force_unicode

setup_environ(settings)


def process_docstring(app, what, name, obj, options, lines):
    # This causes import errors if left outside the function
    from django.db import models
    
    # Only look at objects that inherit from Django's base model class
    if inspect.isclass(obj) and issubclass(obj, models.Model):
        # Grab the field list from the meta class
        fields = obj._meta._fields()
    
        for field in fields:
            # Decode and strip any html out of the field's help text
            help_text = strip_tags(force_unicode(field.help_text))
            
            # Decode and capitalize the verbose name, for use if there isn't
            # any help text
            verbose_name = force_unicode(field.verbose_name).capitalize()
            
            if help_text:
                # Add the model field to the end of the docstring as a param
                # using the help text as the description
                lines.append(u':param %s: %s' % (field.attname, help_text))
            else:
                # Add the model field to the end of the docstring as a param
                # using the verbose name as the description
                lines.append(u':param %s: %s' % (field.attname, verbose_name))
                
            # Add the field's type to the docstring
            lines.append(u':type %s: %s' % (field.attname, type(field).__name__))
    
    # Return the extended docstring
    return lines  
  
def setup(app):
    # Register the docstring processor with sphinx
    app.connect('autodoc-process-docstring', process_docstring)  