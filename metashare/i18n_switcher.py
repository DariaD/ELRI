import logging
from django.conf import settings
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
## Setup logging support.
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(settings.LOG_HANDLER)

def switch_lang_code(path, language):
 
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]
 
    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)
 
    # Split the parts of the path
    parts = path.split('/')
 
    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
        activate(language)
    else:
        parts[0] = "/" + language
        activate(language)
    activate(language)
    
    # Return the full new path
    return '/'.join(parts)

from django import template
from django.template.defaultfilters import stringfilter
 
def switch_i18n_prefix(path, language):
    """takes in a string path"""
    return switch_lang_code(path, language)
 
def switch_i18n(request):
    """takes in a request object and gets the language and the path from it"""
    language=request.POST.get('language', request.GET.get('language'))
    request.session['django_language']=language
    request.LANGUAGE_CODE = language
    current_url=request.POST.get('path', request.GET.get('path'))
    url=switch_lang_code(current_url, language)
    return HttpResponseRedirect(url)
