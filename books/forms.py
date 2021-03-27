from django import forms

from .models import Comments

class CommentBookForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)