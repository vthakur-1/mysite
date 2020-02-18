from django import forms
from allauth.account.forms import SignupForm
from .models import Profile, Album , Photo
from django.forms import ModelForm

from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    type = (
        ('p', 'Photographer'),
        ('c', 'Customer'),
    )
    profile_type = forms.CharField(widget=forms.Select(choices=type))
    first_name = forms.CharField(max_length=100)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.save()
        p = Profile(profile_type=self.cleaned_data['profile_type'], user=user)
        p.save()
        return user


class CustomerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PhotographerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']


class AlbumAddForm(ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'profile']
        widgets = {'profile': forms.HiddenInput()}


class AlbumAddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'album', 'image', 'tag']
        widgets = {'album': forms.HiddenInput()}
