from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
################################################################
from emails.models import Subscriber
from .models import Post, Comment
################################################################
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentModelForm
from emails.forms import SubscriberForm
################################################################
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.detail import SingleObjectMixin
################################################################

# Create your views here.

# homepage related views

#make the homepage a CreateView in order to render subscriber form and SAVE the subscriber  AND send email.
class HomeTemplateView(CreateView):
    model = Subscriber
    form_class = SubscriberForm
    success_url = reverse_lazy('my_blog:home')
    
    #the template thats going to be used is the homepage template
    def get_template_names(self):
        return ['my_blog/home.html']

    #enable use of {{subscriber_form}} in html instead of default {{form}}
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['subscriber_form'] = context['form']
        return context

    #need this method in order to send a subscription email.
    def form_valid(self, form):

        #initialize important email values
        instance_name = form.cleaned_data.get('f_name') #GET the instance first name
        instance_email = form.cleaned_data.get('email') #GET the instance email
        sbj = 'My blog Newsletter Subscription'
        msg = f'Thank you for subscribing {str.capitalize(instance_name)}. You are now going to get an email notifying you whenever there is a new post!'
        
        #send the mail through this function
        send_mail(
            subject= sbj,
            message = msg,
            from_email= settings.EMAIL_HOST_USER, # look at seetings for email configurations, .env file(same dir as settings file) and environ needed
            recipient_list= [instance_email],
            fail_silently= False
        )
        return super(HomeTemplateView, self).form_valid(form)




class HomeRedirectView(RedirectView): #this redirects from www.ex.com/ to www.ex.com/home/ . look at app urls
    url= 'home/'

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#post/draft related views

class PostCreate(LoginRequiredMixin,CreateView):
    form_class = PostForm
    success_url = reverse_lazy('my_blog:home')
    template_name = 'my_blog/Post_form.html'
    #space for method to send mass emails to subscribers
    #when a new post is created

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.filter(draft = False)

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'my_blog/update_post.html'
    success_url = reverse_lazy('my_blog:post_list')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'my_blog/delete_post_confirm.html'
    success_url = reverse_lazy('my_blog:post_list')

######################################################################## 
   
"""We need the detail view to show form for comments and embed the form
functionalities in the same template. NEED it to be a detailview, so we cant
convert it to createview, like we did for the subscribers/home view."""

class PostDetailView(DetailView):
    model = Post

# get context data to use {{comment_form}} in html instead of {{form}}
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = context['form']
        return context

#in the detailview we RENDER the form from our modelform. ONLY RENDER. no functionalities yet
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentModelForm()
        return context

"""the idea is to render form in detailview. after that we make a 'dual' view
Check the comment related views for the next steps"""

#################################################################################

class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'draft_list'
    queryset = Post.objects.filter(draft = True)
    
    #this method is required to be able to make the LIST VIEW choose 
    #a template that has a different name than default, "model"_list.html
    def get_template_names(self):
        return ['my_blog/Draft_list.html']

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#search funcionality view
class SearchResultsView(ListView):
    model = Post

    #the search is going to return a page structured exactly as the Post_list.html
    template_name = 'my_blog/Post_list.html'

    # this method is required for complex queries in the search bar. Notice, it only has to search posts, NOT drafts
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list =  Post.objects.filter(
            Q(post_title__icontains=query) | Q(post_main__icontains=query) | Q(author_f_name__icontains=query) | Q(author_l_name__icontains=query), draft = False
        )
        return object_list

    #we can also return a brand new page by following the code bellow:
    """
    def get_template_names(self):
        return ['my_blog/search_results.html']

    #context data is needed to be able to include the search terms in the template
    # for example when you want the page header to say: "Search results for "SEARCH TERM""
    
    def get_context_data(self):
        context = super(SearchResultsView, self).get_context_data()
        context['query'] = self.request.GET.get('q') # the term 'q' refers to what is defined as a name in the corresponding html. its a GET request
        return context
    
    """

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#comment related views

"""After we rendered the form in the detailview, create a Formview.
FormView is important to specify which template to use,
the fact that its a POST request(IMPORTANT), and that it makes use of 
SingleObjectMixin(IMPORTANT)"""

class CommentCreate(SingleObjectMixin, FormView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'my_blog/Post_detail.html'

    success_url = '#' #by making use of '#' we redirect to the specific post detailview after success

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


"""this is where the magic happens. this is the dual view we planned for.
this view tells us that on a GET request, render the detailview(which renders the form and the blog post).
On POST request (i.e. after form completion and submition), 
give the post id its corresponding pk(IMPORTANT), SAVE and use the success url
from the above form(i.e. http://host/post_detail/8/#) """

class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreate.as_view()
        form = CommentModelForm(request.POST) #(IMPORTANT)
        form.instance.post_id = self.kwargs['pk'] #(IMPORTANT)
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)
    

"""THIS (PostView) view we want to use in our urls.py in place of 
the simple detailview. 
this way we have both rendering and form functionality"""










