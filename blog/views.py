from django.shortcuts import render, get_object_or_404, reverse, redirect, resolve_url
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


def contact(request):
    """to render the contact page"""
    return render(request, 'contact.html')



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6



class DetailBlog(View):
    """View to read the blog post in detail"""
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "detail_blog.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail_blog.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


# Delete a comment
@login_required
def delete_comment(request, comment_id):
    """View to delete a comment"""
    comment =  get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted successfully')
    return HttpResponseRedirect(reverse('detail_blog', args=[comment.post.slug]))



class EditComment(UpdateView):
    """View to edit a comment"""
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Your comment is successfully updated'