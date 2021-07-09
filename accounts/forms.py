from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField,AuthenticationForm, PasswordChangeForm
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.get('instance', None)
        self.fields['icon'].widget.attrs['class'] = 'form-control'
        self.fields['introduction'].widget.attrs['class'] = 'form-control'
        self.fields['nickname'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = User
        fields = (
            "icon", "introduction", "nickname",
        )

class ProfileForm(forms.Form):
    nickname = forms.CharField(max_length=30, label='nickname')
    introduction = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    icon = forms.ImageField(required=False, )
 
class UserPasswordChangeForm(PasswordChangeForm):
    pass
    

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'



