from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import *

class BoardView(ListView):
    model = Ads
    template_name = 'index.html'
    context_object_name = 'ads'


# class CategoryView(ListView):
#     model = Ads
#     template_name =
#     context_object_name = 'ads'
#
#
# class BoardCreate(CreateView):
#     model = Ads
#     template_name =
#
#
# class CommentList(ListView):
#     model = Comment
#     template_name =
#     context_object_name = 'comment'
#
#
# class CommentAcceptView(UpdateView)





