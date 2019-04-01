from django.conf import settings


def base_site_context(request):
    """ base_site_context
    """
    # passing env and debug values to templates
    # context = {'ENVIRONMENT': settings.ENVIRONMENT, 'DEBUG': settings.DEBUG}
    context = {'DEBUG': settings.DEBUG}
    return context