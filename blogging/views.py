from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blogging.serializers import UserSerializer, GroupSerializer, PostSerializer, CategorySerializer
from blogging.models import Post, Category

class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint to allow user view/edit """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ API endpoint to allow gorup view/edit """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """ API endpoint to allow post view/edit """
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """ API endpoint to allow category view/edit """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post':post}
    return render(request, 'blogging/detail.html', context)
