# Create your views here.
from django.shortcuts import render,redirect
# Render: Displays a template with data on the same URL.
# Redirect: Sends the user to a different URL after processing.

from django.contrib.auth.mixins import UserPassesTestMixin# it deny the request until permision allowed
#The UserPassesTestMixin in Django is like a security guard at a door who checks if you meet certain conditions before letting you in.

from django.views.generic import( ListView, 
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from . models import Post # import our databse
# 
# posts = [#dummy data of the post
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()# it access to all database query 
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):#Render some list of objects,
    model = Post
    template_name = 'blog/home.html'#<app>/<model>_<viewtype>.html
    context_object_name = 'posts'# use the home posts content
    ordering = ['-date_posted']# it order the postes by date_poste model 
    paginate_by = 2 # paginate home with 2 content

class PostDetailView(DetailView):#Render a "detail" view of an object.
    model =Post


class PostCreateView(CreateView):# create view in the frontend
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):# overide the form valid method allow us to add the author before the form is submeted
        form.instance.author = self.request.user # it means befor the submiting take the instance and set the author equal curent login user
        return super().form_valid(form)#If the form is valid, save the associated model.
    
class PostUpdateView(UserPassesTestMixin,UpdateView):# update the post view in the fronted
    model = Post
    fields = ['title', 'content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):# this check if the post user is it self he/she is aollwed to update the postc
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

class PostDeleteView(DeleteView):# Delete the post in the frontend class

    model = Post
    
    success_url = '/'# if we delete the post it redirect us to the home pa
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False
    
        



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})