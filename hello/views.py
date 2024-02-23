from django.http import HttpResponse


def hello_view(request):
    name = request.GET.get('name', 'User')
    message = request.GET.get('message', 'Have a nice day')

    result = f'Hello, {name}! {message}'
    return HttpResponse(result)
