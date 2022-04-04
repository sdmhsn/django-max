# from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm


# Create your views here.
class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    # ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.order_by('-date')[:3] # my code experiment. combined between ordering -date and slicing
        return data

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/index.html', {'posts': latest_posts})


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    # ordering = ['-date']
    context_object_name = 'all_posts'

    def get_queryset(self): # my code experiment for ordering the post by -date
        base_query = super().get_queryset()
        data = base_query.order_by('-date')
        return data

# def posts(request):
    # all_posts = Post.objects.all().order_by('-date')
    # return render(request, 'blog/all-posts.html', {'all_posts': all_posts})


class PostDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post  # It will also automatically raise a 404 error

    # context for post_tags
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        context['comment_form'] = CommentForm()
        return context

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     # identified_post = Post.objects.get(slug=slug)
#     return render(request, 'blog/post-detail.html', 
#         {
#             'post': identified_post,  # we don't need to use this code in cbv
#             'post_tags': identified_post.tags.all()
#         }
#     )
