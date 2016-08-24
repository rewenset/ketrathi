from django.shortcuts import render


def index(request):
    template_name = 'book/index.html'
    context = {
        'authenticated': ''
    }
    if request.user.is_authenticated():
        context['authenticated'] = 'You are authenticated with username <i>' \
                                   + request.user.username + '</i>.'
    else:
        context['authenticated'] = 'You are not authenticated.'

    return render(request, template_name, context)
