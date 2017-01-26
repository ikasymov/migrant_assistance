from django import forms

from assistant.models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')