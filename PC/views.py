from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def team(request):
    return render (request, 'team.html')

def testimonial(request):
    return render (request, 'testimonial.html')

def why(request):
    return render (request, 'why.html')