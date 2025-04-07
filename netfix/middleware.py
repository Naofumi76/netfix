from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Paths that don't require login
        self.public_paths = [
            '/register/',
            '/register/company/',
            '/register/customer/',
            '/register/login/',
            '/admin/',
        ]
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            
            # Skip authentication check for public paths
            if any(path.startswith(public_path) for public_path in self.public_paths):
                return self.get_response(request)
            
            # Allow home page without login
            if path == '/':
                return self.get_response(request)
            
            return redirect('/register/login/')
        
        return self.get_response(request)
