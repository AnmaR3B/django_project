from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 
from django.views.generic import ListView
# def post_list(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list,3)
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger: 
#         posts =  paginator.page(1) 

#     return render(request, 'blog/post/list.html', {'posts':posts}) # sending context for template list.html

class PostListView(ListView):
    """
    Alternative post list view """
    model = Post
    content_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year,month,day,post):
#def post_detail(request, id):
   # method-1 
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found")
    # return render(request, 'blog/post/detail.html', {'post': post})

   # method-2
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day,                 
            )
    return render(request, 'blog/post/detail.html', {'post':post})
