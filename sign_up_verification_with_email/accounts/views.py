from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {
        'home': 'Home View'
    }
    return render(request, 'base.html', context)
