from django import forms
#to import and create form frommodel
from .models import Review
from django.forms import ModelForm

""" class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=100)
    last_name = forms.CharField(label='Last Name',max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label = 'Write your review here',
                            widget=forms.Textarea(attrs={'class':'myform','rows':'5','cols':'50'}))

 """
 #makes a form for the model
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #to specify which fields from the model:
        # fields = ['first_name','last_name','stars']

        #to ask all fields to show:
        fields = "__all__"
        #to manually name the labels create a dict and assign KeyValues 
        #as the actual model name attributes and the string to display
        labels = {
            'first_name':'YOUR FIRST NAME',
            'last_name':'YOUR LAST NAME',
            'stars':'Rating'
        }
##to customize error messages in forms. 
        error_messages = {
            'stars':{
                'min_value':"MIN VALUE IS 1 !!",
                'max_value':"MAX VALUE IS 5 !!"
            }
        }

