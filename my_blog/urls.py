from django.urls import path
from .views import (HomeTemplateView, PostCreate, PostDetailView, PostListView, 
                    DraftListView, HomeRedirectView, SearchResultsView, 
                    UpdatePostView, DeletePost, PostView)
from django.conf.urls.static import static
from django.conf import settings

app_name = 'my_blog' #important for the project to specify app names. Easy reference for use in views and html


urlpatterns = [

    path('home/', HomeTemplateView.as_view(), name = 'home'),
    path('',HomeRedirectView.as_view(), name='home_redirect'),
    path('create/', PostCreate.as_view(), name = 'create_post'),
    path('post_list/', PostListView.as_view(), name = 'post_list'),
    path('draft_list/', DraftListView.as_view(), name = 'draft_list'),
    path('search/', SearchResultsView.as_view(), name = 'search_results'),
    path('post_detail/<int:pk>/', PostView.as_view(), name = 'post_detail'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name = 'update_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name = 'delete_post'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

"""+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) is ONLY for development
it helps create the file on the specified path (defined in settings.py and model's post_image field) on upload, and
it helps GET the post thumbnails when they are already uploaded by user, for 
rendering in the post list template"""