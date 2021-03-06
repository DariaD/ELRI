import logging
from django.utils import translation
from django.utils.translation import ugettext as _
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from metashare.repository.models import resourceInfoType_model
from metashare.settings import LOG_HANDLER, COUNTRY, LANGUAGE_CODE
from metashare.storage.models import PUBLISHED

# Setup logging support,
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(LOG_HANDLER)

#issue 69: temporal fix
#translation.activate(LANGUAGE_CODE)

#Custom authentication error messages: 
class ELRIAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _("Please enter a correct username and password. Note that both "
            "fields may be case-sensitive. ")+_("Please contact us if there is any issue with an existing account."),
        'inactive': _("Please enter a correct username and password. Note that both "
            "fields may be case-sensitive. ")+_("Please contact us if there is any issue with an existing account."),
        #'inactive':_("This account has not been activated yet. Please contact us if there is any issue with an existing account."), 
        }

def frontpage(request):
    """Renders the front page view."""
    #issue 69: temporal fix
    #request.session['django_language'] = LANGUAGE_CODE
    #request.LANGUAGE_CODE = LANGUAGE_CODE
    
    LOGGER.info(u'Rendering frontpage view for user "{0}".'
                .format(request.user.username or "Anonymous"))
    lr_count = resourceInfoType_model.objects.filter(
        storage_object__publication_status=PUBLISHED,
        storage_object__deleted=False).count()
    dictionary = {'country': COUNTRY}
    return render_to_response('frontpage.html', dictionary,
      context_instance=RequestContext(request))


def login(request, template_name, redirect_field_name=None, authentication_form=ELRIAuthenticationForm ):
    """Renders login view by connecting to django.contrib.auth.views."""
    LOGGER.info(u'Rendering login view for user "{0}".'.format(
      request.user.username or "Anonymous"))

    return auth_views.login(request, template_name, redirect_field_name, authentication_form)


def logout(request):
    """Renders logout view by connecting to django.contrib.auth.views."""
    LOGGER.info(u'Logging out user "{0}", redirecting to /.'.format(
      request.user.username or "Anonymous"))

    return auth_views.logout(request, 'frontpage')

from django.http import HttpResponse, FileResponse, Http404
from metashare.settings import STATIC_ROOT

def pt_pdf_view(request):
    pt_path=STATIC_ROOT+'/metashare/aspetosfuncionais_pt-pt.pdf'
    print(pt_path)
    #try:
    #    return FileResponse(open(pt_path,'rb'),content_type='application/pdf')
    #except:
    #    raise Http404()
    with open(pt_path, 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        #response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    ##pdf.closed