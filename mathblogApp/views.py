from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import Post

class PostListView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		context['posts'] = posts
		return render(request, "mathblog/post_list.html", context)

post_list = PostListView.as_view()