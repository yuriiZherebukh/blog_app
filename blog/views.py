from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json
from .models import Post
from .forms import PostForm


class PostView(View):

    def get(self, request, post_id=None):
        if not post_id:
            posts = Post.get_all()
            print(posts)
            posts = [post.to_dict() for post in posts]
            print(posts)
            return render(request, 'blog/post_list.html', {'posts': posts})
        else:
            print(post_id)
            post = Post.get_by_id(post_id)
            post = post.to_dict()
            return JsonResponse(post, status=200)

    def put(self, request, post_id=None):
        print(request.method)
        post = Post.get_by_id(post_id)
        if not post:
            return HttpResponse(status=404)
        update_data = json.loads(request.body.decode('utf-8'))
        post.update(**update_data)
        return JsonResponse(post.to_dict(), status=200)

    def post(self,request):
        post_data = json.loads(request.body.decode('utf-8'))
        print(request.body)
        post = Post()
        post.create(**post_data)
        post.publish()
        return JsonResponse(post.to_dict(),status=200)

    # def delete(self,post_id):
    #     print(post_id)
    #     post = Post.get_by_id(post_id)
    #     if not post:
    #         return HttpResponse(status=404)
    #     #post.delete()
    #     return JsonResponse(post,status=200)

