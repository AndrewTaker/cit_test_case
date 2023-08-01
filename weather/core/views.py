from django.shortcuts import render

NOT_FOUND = 404
CSRF_FAILURE = 403
INTERNAL_SERVER_ERROR = 500


def page_not_found(request, exception):
    template_name = 'core/404.html'
    context = {'path': request.path}
    status = NOT_FOUND
    return render(request, template_name, context, status=status)


def csrf_failure(request, reason=''):
    template_name = 'core/403csrf.html'
    status = CSRF_FAILURE
    return render(request, template_name, status=status)


def internal_server_error(request):
    template_name = 'core/500.html'
    context = {'path': request.path}
    status = INTERNAL_SERVER_ERROR
    return render(request, template_name, context, status)
