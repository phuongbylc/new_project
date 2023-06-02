from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.

class IndexClass(View):
    def get(self, request):
        return render(request, 'Index.html')
    
class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

class HomeClass(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the home.")
