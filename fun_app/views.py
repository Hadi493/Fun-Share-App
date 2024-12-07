from django.shortcuts import render # type: ignore
from functools import wraps
from django.http import HttpResponse

def skip_ngrok_warning(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        
        # Convert HttpResponse to a modifiable response if it isn't already
        if isinstance(response, HttpResponse):
            response_obj = response
        else:
            response_obj = HttpResponse(response)
            
        # Set all possible variations of the header
        response_obj['ngrok-skip-browser-warning'] = 'true'
        response_obj['Ngrok-Skip-Browser-Warning'] = 'true'
        response_obj['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        
        return response_obj
    return wrapped_view

@skip_ngrok_warning
def home(request):
    response = render(request, 'index.html')
    return response
