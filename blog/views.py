from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import post,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .form import ContactForm

# static demo data
# posts =[
#         {"id":1,"title":'post 1' ,'content':'content of post 1'},
#         {"id":2,"title":'post 2' ,'content':'content of post 2'},
#         {"id":3,"title":'post 3' ,'content':'content of post 3'},
#         {"id":4,"title":'post 4' ,'content':'content of post 4'},
#         {"id":5,"title":'post 5' ,'content':'content of post 5'},
#         {"id":6,"title":'post 6' ,'content':'content of post 6'},
#     ]


def index(request):
    tittle ="Anime info.." 

    # getting data from post model
    all_posts= post.objects.all()


    #    paginator
    paginator = Paginator(all_posts,6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request,"index.html",{'tittle':tittle,'page_obj':page_obj})


def detail(request,post_id):
     # static
    # post1= next((item for item in posts if item['id'] == int(post_id)),None)
    try:
        # getting fata from model
        post1=post.objects.get(pk=post_id)
        related_posts = post.objects.filter(category = post1.category)

    except post.DoesNotExist:
        raise Http404("post dose not Exist")
   
    

    # logger=logging.getLogger("TESTING")
    # logger.debug(f"post variable is{post1}")
    return render(request,"details.html",{'post1':post1, 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_view(request):
    return HttpResponse("this is the new url ")    


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name =request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        logger=logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"post variable is{form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message ="your message have been send"
            return render(request,"contact.html",{'form':form, 'success_message':success_message}) 
        else:
            logger.debug('form validation failure') 
        return render(request,"contact.html",{'form':form, 'name':name, 'email':email, 'message':message})  
    return render(request,"contact.html")         
        

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,"about.html",{"about_content":about_content})        
        

   
    
      

       
     