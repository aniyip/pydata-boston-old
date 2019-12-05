from django.shortcuts import render

# Create views found in pages/templates directory
# These will also be referenced in pages/urls.py

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def meetups(request):
    return render(request, "meetups.html", {})

def getinvolved(request):
    return render(request, "get-involved.html", {})