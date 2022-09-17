from tkinter import Widget
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.

#Database table for all the posts. If draft==True then the post is considered a DRAFT.
#drafts are handled differently, as they require admin privileges to view
class Post(models.Model):
    author_f_name = models.CharField(max_length = 30, verbose_name = 'First Name')
    author_l_name = models.CharField(max_length = 30, verbose_name='Last Name')
    author_email = models.EmailField()
    creation_date = models.DateTimeField(default = timezone.now, verbose_name = 'Time of creation')
    publication_date = models.DateTimeField(blank = True, null = True)
    post_title = models.CharField(max_length = 600, verbose_name = 'Title')
    draft = models.BooleanField(default = True, verbose_name= 'Is this a Draft?(check the box if YES)')
    post_image = models.ImageField( upload_to = "thumbnails/", height_field = None, width_field = None, max_length=100, blank = True, null = True, verbose_name = 'Post Thumbnail')
    post_main = RichTextField(blank = True, null = True, max_length = None,verbose_name = "")
    

    #this will be a button to publish a post out of a list of draft posts, or the current one
    def publish_post(self):
        if self.draft == True :
            self.draft = False
            self.publication_date = timezone.now
            self.save()
        
    #this will be the button to save a post to a list of draft posts, without publishing
    #the posts will be displayed in two different pages, depending if they are drafts of not
    #this will happen in the views section

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.post_title


#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------


#database table for comments. commenters just provide their info and can add a comment.
#no special handling needed, but we store the comments. SIDENOTE: apply analytics later on.
class Comment(models.Model):
    post = models.ForeignKey('my_blog.Post',on_delete=models.CASCADE, related_name='comments')
    comment_title = models.CharField(max_length=600, verbose_name='Title')
    nickname = models.CharField(max_length=100, verbose_name='UserName')
    comment_content = models.TextField(max_length=None, verbose_name='Leave a Comment...')
    create_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_content



#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

