from django import forms

from blog.models import BlogPost, Comment


class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
