from datetime import datetime

from django import forms
from django.forms import DateTimeInput

from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'pub_date': DateTimeInput(attrs={'placeholder': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}),
        }
        fields = [
            'title',
            'description_short',
            'description_long',
            'url_assert',
            'category',
            'pub_date'
        ]
