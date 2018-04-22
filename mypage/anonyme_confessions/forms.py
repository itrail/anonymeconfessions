from django import forms
from .models import Article, User, Comment
from django.core.validators import RegexValidator

class AddArticleForm(forms.ModelForm):
    title =  forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Tytuł'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Tu wpisz zawartość wyznania'}))
    keywords = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Tagi'}))
    class Meta:
        model = Article
        fields = ('title', 'content', 'keywords', )
    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['content'].label = ""
        self.fields['keywords'].label = ""
form = AddArticleForm()

class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Potwierdź hasło'}),
    )
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""
        self.fields['confirm_password'].label = ""

class CommentingForm(forms.ModelForm):
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Napisz Komentarz...'}))

    class Meta:
        model = Comment
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super(CommentingForm, self).__init__(*args, **kwargs)
        self.fields['comment'].label = ''