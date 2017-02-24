from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ("published_date", "post",)