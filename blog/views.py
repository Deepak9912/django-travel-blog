from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Post, Contact, Comment
from .forms import CommentForm, ContactForm
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

# view for detailed blog post
class DetailBlog(View):

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

#Edit a comment
class CommentEditView(UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'comment_edit.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('detail_blog', args=[slug])



# view for contact form
class ContactFormView(FormView):

    def post(self, request, *args, **kwargs):
        template_name = 'contact/base.html'
        form = ContactForm(data=request.POST)
        success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
        return render(request, "base.html", {'form': form})
