from django import forms
from django.contrib.auth.models import User
from foot.models import UserProfile, Author
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('first_name','last_name','email')
