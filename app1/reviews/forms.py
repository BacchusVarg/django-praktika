from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {
            "name": "Ваше имя",
            "text": "Текст отзыва"
        }
        fields = ['name', 'text']