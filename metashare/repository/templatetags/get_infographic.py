from django import template
from django.conf import settings
import logging


LOG = logging.getLogger(__name__)


register = template.Library()


@register.assignment_tag
def get_infographic(lang):
    """Returns a localized url for the download of the user_guidelines.
    """
    elri_infographic='metashare/Irish_NRS_Infographic_'+lang+'.pdf'
    return elri_infographic
    
