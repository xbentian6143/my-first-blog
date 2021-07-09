from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from .forms import PostCreateForm,IdeaCreateForm,ProposalCreateForm
from .models import Post, Idea, Proposal, Sympathy, Good
from django.utils import timezone
import datetime
import sys
sys.path.append('../')
from accounts.models import User
from django.utils.timezone import make_aware
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from operator import attrgetter,itemgetter

 

 



# Create your views here.
def post_list(request):
    
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    posts_with_sympathy_counts = Post.objects.annotate(sympathy_num = Count('sympathy')).order_by('-sympathy_num')
    

    if  request.user.is_authenticated:
        sympathy_list = Sympathy.objects.filter(user = request.user)
        sympathy_post_list = [sympathy.target for sympathy in sympathy_list]

        return render(request, 'post/post_list.html',
                    {'posts':posts,
                    'posts_with_sympathy_counts':posts_with_sympathy_counts,
                    'sympathy_post_list':sympathy_post_list
                    }
                )

    else :
        
        return render(request, 'post/post_list_ano.html',
                    {'posts':posts,
                    'posts_with_sympathy_counts':posts_with_sympathy_counts,
                    })


@login_required
def post_create(request):

    if request.method == "POST":
        
        form = PostCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.published_date = make_aware(datetime.datetime.now())
            instance.save()
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
    return render(request, 'post/post_create.html', {'form': form})


def post_detail(request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        ideas = Idea.objects.filter(target = post).order_by('-published_date')
        ideas_count=ideas.count()
        sympathys_count = Sympathy.objects.filter(target = post).count()
        ideas_with_good_counts = Idea.objects.filter(target = post).annotate(good_num = Count('good')).order_by('-good_num')

        if  request.user.is_authenticated:

            good_list = Good.objects.filter(user = request.user )
            good_idea_list = [good.target for good in good_list ]
            sympathy_list = Sympathy.objects.filter(user = request.user)
            sympathy_post_list = [sympathy.target for sympathy in sympathy_list]

        
            
            return render(request, 'post/post_detail.html', 
                        {'ideas': ideas,
                        'ideas_count':ideas_count,
                        'ideas_with_good_counts':ideas_with_good_counts,
                        'post': post,
                        'sympathys_count':sympathys_count,
                        'good_idea_list':good_idea_list,
                        'sympathy_post_list':sympathy_post_list
                    })
        else :
            return render(request, 'post/post_detail_ano.html', 
                        {'ideas': ideas,
                        'ideas_count':ideas_count,
                        'ideas_with_good_counts':ideas_with_good_counts,
                        'post': post,
                        'sympathys_count':sympathys_count,
                    })




def post_delete_confirm(request, post_pk):

    return render(request, 'post/post_delete_confirm.html', {'post_pk':post_pk})


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('post:post_list')

def idea_delete_confirm(request, idea_pk,post_pk):

    return render(request, 'post/idea_delete_confirm.html', {
                'idea_pk':idea_pk,
                'post_pk':post_pk
                })


def idea_delete(request,idea_pk):
    idea = get_object_or_404(Idea, pk=idea_pk)
    idea.delete()
    return redirect('post:post_detail', post_pk=idea.target.pk)


@login_required
def idea_create(request,pk):
    
    if request.method == "POST":
        
        form = IdeaCreateForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=pk)
            idea = form.save(commit=False)

            idea.author = get_object_or_404(User, email=request.user.email)
            idea.target = post
            idea.published_date = make_aware(datetime.datetime.now())
            idea.save()
        return redirect ('post:post_detail', post_pk = pk)
        

    else:
        post = get_object_or_404(Post, pk=pk)
        form = IdeaCreateForm()
        context = {
                'form': form,
                'post': post,
            }
    return render(request, 'post/idea_create.html',context)

 


@login_required 
def sympathy1(request,post_pk,sympathys_count):
   
    if request.method == 'POST':
        query = Sympathy.objects.filter(user = request.user, target=get_object_or_404(Post, pk=post_pk))
        liked = False
        if query.count() == 0:
            sympathy = Sympathy()
            sympathy.user = request.user
            sympathy.target = get_object_or_404(Post, pk=post_pk)
            sympathy.created_date = make_aware(datetime.datetime.now())
            sympathy.save()
            liked= True
            sympathys_count = sympathys_count
        else:
            sympathys_count = sympathys_count - 1
            query.delete()


        context = {
            'post_pk' : post_pk,
            'liked' : liked,
            'sympathys_count':sympathys_count,
        }

    return JsonResponse(context)



@login_required 
def sympathy2(request,post_pk,sympathys_count):
   
    if request.method == 'POST':
        query = Sympathy.objects.filter(user = request.user, target=get_object_or_404(Post, pk=post_pk))
        liked = False
        if query.count() == 0:
            sympathy = Sympathy()
            sympathy.user = request.user
            sympathy.target = get_object_or_404(Post, pk=post_pk)
            sympathy.created_date = make_aware(datetime.datetime.now())
            sympathy.save()
            liked= True
            sympathys_count = sympathys_count + 1
        else:
            sympathys_count = sympathys_count
            query.delete()

        context = {
            'post_pk' : post_pk,
            'liked' : liked,
            'sympathys_count':sympathys_count,
        }

    return JsonResponse(context)







@login_required 
def good1(request,idea_pk,goods_count):
    
    
    if request.method == 'POST':
        query = Good.objects.filter(user = request.user, target=get_object_or_404(Idea, pk=idea_pk))
        liked = False
        if query.count() == 0:
            good = Good()
            good.user = request.user
            good.target = get_object_or_404(Idea, pk=idea_pk)
            good.created_date = make_aware(datetime.datetime.now())
            good.save()
            liked= True
            goods_count = goods_count 
        else:
            goods_count = goods_count - 1
            query.delete()

        context = {
            'idea_pk' : idea_pk,
            'liked' : liked,
            'goods_count':goods_count,
        }
        
        return JsonResponse(context)


@login_required 
def good2(request,idea_pk,goods_count):
    
    print(idea_pk)
    if request.method == 'POST':
        query = Good.objects.filter(user = request.user, target=get_object_or_404(Idea, pk=idea_pk))
        liked = False
        if query.count() == 0:
            good = Good()
            good.user = request.user
            good.target = get_object_or_404(Idea, pk=idea_pk)
            good.created_date = make_aware(datetime.datetime.now())
            good.save()
            liked= True
            goods_count = goods_count +1
        else:
            goods_count = goods_count 
            query.delete()

        context = {
            'idea_pk' : idea_pk,
            'liked' : liked,
            'goods_count':goods_count,
        }
        
        return JsonResponse(context)
