from django.shortcuts imports render_to_response

def error404(request):
    return render(request, '404.html')

