from cProfile import label
from xml.sax.xmlreader import AttributesImpl
from django import forms
from.models import Post, Comment
from django.forms import ModelForm



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        widgets = {
            'author_f_name' : forms.TextInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'Name Here'}),

            'author_l_name' : forms.TextInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'Last Name Here'}),

            'author_email' : forms.EmailInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'email here'}),

            'creation_date' : forms.DateTimeInput(attrs={'class':'form-control'}),

            'publication_date' : forms.DateTimeInput(attrs={'class':'form-control'}),

            'post_title' : forms.TextInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'Title Here'}),

            'post_main' : forms.Textarea(attrs={'class':'form-control',
                                                        'id':'floatingTextarea',
                                                        'placeholder':'Post Here'}),

            'post_image' : forms.ClearableFileInput(attrs={'class':'form-control'})
        }

################################################################################################
################################################################################################
################################################################################################

class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'comment_title', 'comment_content']

        widgets = {

            'nickname': forms.TextInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'Nickname Here'}),


            'comment_title' : forms.TextInput(attrs={'class':'form-control',
                                                        'id':'floatingInput',
                                                        'placeholder':'Title Here'}),

            'comment_content' : forms.Textarea(attrs={'class':'form-control',
                                                        'id':'floatingTextarea',
                                                        'placeholder':'Comment Here',
                                                        'style':'height:15%;'}),

        }