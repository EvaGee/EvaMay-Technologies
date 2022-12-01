from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Blog

def index(request):
  mymembers = Blog.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  blog = Blog(firstname=x, lastname=y)
  blog.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  blog = Blog.objects.get(id=id)
  blog.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  myblog = Blog.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': myblog,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  blog = Blog.objects.get(id=id)
  blog.firstname = first
  blog.lastname = last
  blog.save()
  return HttpResponseRedirect(reverse('index'))