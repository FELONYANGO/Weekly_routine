from django.shortcuts import render

# landing page home view
def home(request):
    return render(request,"home.html")
