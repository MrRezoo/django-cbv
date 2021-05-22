from django import forms

from first.models import Comment


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=200)


class TodoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
