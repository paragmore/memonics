from django import forms
from django.forms import inlineformset_factory
from .models import Post, PostImage, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Add a comment...'})
        # this overwrites the input for content field and lets you update attrs of that input <input>


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['caption'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Add a caption...'})
        self.fields['content'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Add details'})

class ImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['modelimage', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelimage'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Add a image'})


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'search'})
