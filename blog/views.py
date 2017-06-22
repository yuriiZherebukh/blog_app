from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


from .models import Post
from .forms import PostForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = ['title','text','image']
    template_name = 'blog/post_edit.html'

    def post(self, request):
        self.form = PostForm(request.POST)
        if self.form.is_valid():
            self.post = self.form.save(commit=False)
            self.post.author = request.user
            self.post.published_date = timezone.now()
            self.post.save()
            return redirect('post_detail', pk=self.post.pk)
        return render(request, 'blog/post_edit.html', {'form': self.form})


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','text','image']
    template_name = 'blog/post_edit.html'

    def post(self,request,*args,**kwargs):
        self.post = Post.objects.get(pk=self.kwargs['pk'])  # model and primary key for article
        self.form = PostForm(request.POST, instance=self.post)  # pass this 'post'
        if self.form.is_valid():
            self.post = self.form.save(commit=False)
            self.post.author = request.user
            self.post.published_date = timezone.now()
            self.post.save()  # queryset,  saves this 'post'
            return redirect('post_detail', pk=self.post.pk)
        return render(request, 'blog/post_edit.html', {'form': self.form})


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')


