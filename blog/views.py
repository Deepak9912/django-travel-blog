from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, FormView
from .models import Post, Comment, Contact
from .forms import PostForm, CommentForm, ContactForm


# view for list of posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    


# view for detailed blog post
class DetailBlog(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        post = Post.object.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'detail_blog.html', context)


    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'detail_blog.html', context)


#Edit a comment
class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'content', 'body']
    template_name = 'post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('detail_blog', kwargs={'pk': pk})




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