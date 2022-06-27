from django import forms
from .models import Posts, Category

choices = Category.objects.all().values_list('name', 'name')
choices_l = []
for item in choices:
    choices_l.append(item)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'author', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Let\'s write some title to your Post'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            'category': forms.Select(choices=choices_l, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write title for post'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

