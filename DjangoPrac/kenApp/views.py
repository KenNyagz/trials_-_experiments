#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def hello(request):
    ''' '''
    #return HttpResponse("Hello");
    template = loader.get_template('all_users.html')
    users = User.objects.all().values()
    payload = {
        'theUsers': users
    }
    return HttpResponse(template.render(payload, request))

def details(request, id):
    ''' '''
    #user = User.objects.get(id=id)
    user = User.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    ''' '''
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    ''' '''
    template = loader.get_template('template.html')
    context = {
        'Veggies': ['Cabbage', 'Onion', 'Tomato'],
    }
    return HttpResponse(template.render(context, request))
