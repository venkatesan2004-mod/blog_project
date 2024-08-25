from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import logging
from django.urls import reverse
from .models import post
from django.core.paginator import Paginator
from .forms import Contactform 
# Create your views here.
# static demo data
# posts=(
#     {'id':1,'post':'post1','content':'content1'},
#     {'id':2,'post':'post2','content':'content2'},
#     {'id':3,'post':'post3','content':'content3'},
#     {'id':4,'post':'post4','content':'content4'},
# )

def model(request):
    return HttpResponse("model page is here")
#redirect 
def old_url(request):
    return redirect(reverse("blog:new_url"))
def new_url(request):
    return HttpResponse("here is the new urls")
#return httml

def index(request):
    # Getting data from post model
    posts= post.objects.all()

    #paginatep
    paginator=Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'index.html',{'page_obj':page_obj})



def detail(request,slug):
    #static data
    #post=next((item for item in posts if item['id'] == int(post_id)),None)

#geting data from model by id
   try:
    Post=post.objects.get(slug=slug) 
    
    related_posts=post.objects.filter(category=Post.category).exclude(pk=Post.id)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {Post}')  
    return render(request,"details.html",{'post':Post,"related_posts":related_posts})
   except post.DoesNotExist:
    raise Http404("post id doen't exist")
    
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {Post}')  

def contact(request):
   if request.method=='POST':
      form=Contactform(request.POST)

      if form.is_valid:
        form=Contactform(request.POST or None)
        logger=logging.getLogger("TESTING")
        logger.debug(f'post data is {form.cleaned_data['name']},{form.cleaned_data['email']},{form.cleaned_data['message']}')  
   return render(request,"contact.html")