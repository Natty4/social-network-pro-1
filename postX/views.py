from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from .forms import postUploadForm,cmntForm, SearchForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
 
@login_required 
def uploadPost(request):
	if request.method == 'POST':
		post_form = postUploadForm(request.POST or None, request.FILES or None )
		user = request.user
		if post_form.is_valid():
			post = post_form.save(commit = False)
			post.user = user
			post.save()
			return HttpResponseRedirect('/')
	else:
		post_form = postUploadForm()
	return render(request, 'postX/uploadPost.html', {'post_form':post_form})



@login_required
def userPosts(request):
	posts = Post.published.all()

	paginator = Paginator(posts, 4)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		posts = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request,'postX/list.html', {'posts':posts})
	return render(request,'postX/lst.html', {'posts':posts})

@login_required
def postDetail(request, year, month, day, id):
	print(year, month, day, id)
	post = get_object_or_404(Post, publish__year = year, publish__month = month, publish__day = day, id = id)
	comments = post.comments.filter(active=True)
	form = cmntForm(data=request.POST)
	if request.method == 'POST':
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.user = request.user
			comment.save()
			return render(request, 'postX/detail.html', {'post': post, 'form':form, 'comment': comment, 'comments': comments})
		else:
			form = cmntForm()
	return render(request, 'postX/detail.html', {'post': post, 'form':form, 'comments': comments})
@login_required 
def postSearch(request):
	form = SearchForm()
	query = None
	results = []
	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			search_vector = SearchVector('user', 'post_txt')
			search_query = SearchQuery(query)
			results = Post.published.all().annotate(
				search=search_vector,
				rank=SearchRank(search_vector, 
					search_query)).filter(search=search_query).order_by('-rank')
	return render(request, 'postX/search.html', {'form': form, 'query': query, 'results': results})



@login_required 
def postLike(request):
	post_id = request.POST.get('id')
	action = request.POST.get('action')
	if post_id and action:
		print(post_id)
		print(action)
		try:
			post = Post.published.get(id=post_id)
			for i in post.users_like.all():
				# print(post)
				# print(post.users_like.all())
				if action == 'like':
					post.users_like.add(request.user)
				else:
					post.users_like.remove(request.user)
				return JsonResponse({'status':'ok'})
				
		except:
			pass
	return JsonResponse({'status':'error'})



def postDelete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method =="POST":
		post.status = 0
		post.save()
		return redirect("/") 
	return render(request, 'postX/delete.html', {'post':post})










"""

class CreatePostView(CreateView):
	model = Post
	#form_class = postUploadForm
	#fields = '__all__'
	fields = ['post_txt','post_img']
	success_url = '/' 
	template_name = 'postX/uploadPost.html'

class PostListView(ListView):
	model = Post
	template_name = 'postX/list.html'
class PostDetailView(DetailView):
	template_name = 'postX/detail.html'

	def get_queryset(self):
		year = self.kwargs.get('year')
		month = self.kwargs.get('month')
		day = self.kwargs.get('day')
		qs = Post.published.filter(publish__year=year, publish__month=month, publish__day=day)
		return qs
"""