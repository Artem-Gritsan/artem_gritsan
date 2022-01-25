from django import forms
from django.db.models import fields
from django.forms import widgets, TextInput, FileInput, Textarea
from .models import Post


class AddPostViaModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('pet_type', 'title', 'content', 'breed', 'сontact_person', 'tel', 'locality', 'price', 'image')

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),

            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content'
            }),

            'breed': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter breed'
            }),

            'сontact_person': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact person'
            }),

            'tel': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone'
            }),

            'locality': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter locality'
            }),

            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),

            'image': FileInput(attrs={
                'class': 'form-control-file',
    
            })

        }
# class AddPost(forms.Form):
#     pet_type = forms.ChoiceField(choices=Post.PET_TYPES, label='Post type')
#     title = forms.CharField(label='Title', max_length=40)
#     content = forms.CharField(label='Content', max_length=400, widget=forms.Textarea)
#     breed = forms.CharField(label='Breed', max_length=30)
#     сontact_person = forms.CharField(label='Contact person', max_length=30)
#     tel = forms.CharField(label='Phone', max_length=13)
#     locality = forms.CharField(label='Locality', max_length=30)
#     price = forms.CharField(label='Price', max_length=20)
#     image = forms.ImageField(label='Post image')
        