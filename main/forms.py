from django import forms
from .models import Post,Comment


class Commented(forms.ModelForm):

    class Meta:
        model=Comment
        fields='__all__'
        