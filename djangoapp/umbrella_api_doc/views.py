from django.shortcuts import render

# Create your views here.

def umbrella_api_doc(request):
     return render(request, 'index.html')