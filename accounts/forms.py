from django import forms
from django.core import validators
from django.contrib.auth.models import User, auth




class Login(forms.Form):
    username = forms.CharField(label='UserId')
    password = forms.CharField(widget=forms.PasswordInput())
    #captcha = ReCaptchaField(attrs={'theme': 'clean'})

class Register(forms.Form):


    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(min_length=10, max_length=10, label="UserId")
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password',min_length=6, max_length=14)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')




class Profile(forms.Form):


    first_name = forms.CharField( disabled=True)
    last_name = forms.CharField(disabled=True)
    username = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)

class Mess(forms.Form):
    meal = (('none', 'select'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Dinner', 'Dinner'))
    rate = (('none', 'select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    meal = forms.ChoiceField(choices=meal)
    rating = forms.ChoiceField(choices=rate)
    review = forms.CharField(required=False, max_length=50)

class Student(forms.Form):
    host = (('Aryabhatta', 'Aryabhatta'), ('Ramanujan', 'Ramanujan'), ('C.V Raman', 'C.V Raman'),
            ('Mandakini', 'Mandakini'))
    br = (('IT', 'IT'), ('ME', 'ME'), ('EE', 'EE'))

    fl = (('ground', 'ground'), ('first', 'first'), ('second', 'second'), ('third', 'third'))

    rm = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
          ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'),
          ('15', '15'), ('16', '16'))
    branch = forms.ChoiceField(choices=br,widget=forms.Select())
    hostel = forms.ChoiceField(choices=host)
    floor = forms.ChoiceField(choices=fl)
    RoomNo = forms.ChoiceField(choices=rm)





