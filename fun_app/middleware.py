"""
Middleware to skip ngrok browser warning
"""

class NgrokSkipWarningMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # Set custom headers before the request is processed
        request.META['HTTP_USER_AGENT'] = 'PostmanRuntime/7.32.3'
        request.META['HTTP_NGROK_SKIP_BROWSER_WARNING'] = '1'
        return None

    def __call__(self, request):
        # Process the request first
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
            if response:
                return response
                
        response = self.get_response(request)
        
        # Set response headers
        response['ngrok-skip-browser-warning'] = '1'
        response['User-Agent'] = 'PostmanRuntime/7.32.3'
        response['Access-Control-Allow-Headers'] = 'ngrok-skip-browser-warning'
        response['Access-Control-Allow-Origin'] = '*'
        
        return response