from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.views import View

from post.forms import PostForm
from post.models import Post


class PostListView(View):
	def get(self, request):
		posts = Post.objects.all()
		context = {"posts": posts}
		return render(request, "post_list.html", context)


class PostCreateView(View):
	def get(self, request):
		context = {"form": PostForm}
		return render(request, "post_create.html", context)

	def post(self, request):
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"]
			body = form.cleaned_data["body"]
			author_name = form.cleaned_data["author_name"]
			post = Post.objects.create(title=title, body=body, author_name=author_name)
			return render(request, "post_detail.html", {"post": post})

		posts = Post.objects.all()
		context = {"posts": posts, "errors": form.errors, "form": PostForm}
		return render(request, "post_list.html", context)


class PostDetailView(View):
	def get(self, request, post_id):
		post = get_object_or_404(Post, pk=post_id)
		return render(request, "post_detail.html", {"post": post})


class PostLikeView(View):
	def post(self, request, post_id):
		post = get_object_or_404(Post, pk=post_id)
		post.points = F("points") + 1
		post.save()
		post.refresh_from_db()
		return render(request, "post_detail.html", {"post": post})
