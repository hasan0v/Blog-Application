from django import forms
from .models import Post, Categorie

choices = Categorie.objects.all().values_list('name', 'name')
# choices = Categorie.objects.all().values_list('id', 'id')
choices_l = []
for item in choices:
    choices_l.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Let\'s write some title to your Post'}),
            'category': forms.Select(choices=choices_l, attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write title for post'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_l, attrs={'class':'form-control'}),

        }

