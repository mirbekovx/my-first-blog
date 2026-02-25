from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',) # Мы берем только текст, так как автора и пост добавим в коде