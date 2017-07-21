# if we are making a database driven app we need to make forms
from django import forms

#Forinstance, you might have a BlogComment model, and you want to create a form that lets people submit comments.
#In this case, it would  be redundant to define the field types in your form, because you’ve already defined the fields in your model.
# for this we import files from models.py
from models import UserModel, PostModel, LikeModel, CommentModel

# forms are created using classes which consists of fields that are to be displayed in web pages
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'name', 'email', 'password']

# like pour user formhas fields username and password
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'caption']


class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields = ['post']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']
