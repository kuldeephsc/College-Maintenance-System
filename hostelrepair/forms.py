from django import forms
from django.contrib.auth.models import User

class Repair(forms.Form):
    objects = (('none', 'select'), ('fan', 'fan'), ('tubelight', 'tubelight'), ('switch board', 'switch board'), ('bed', 'bed'),
           ('chair', 'chair'), ('table', 'table'), ('cupboard', 'cupboard'), ('door', 'door'))

    host = (('none', 'select'), ('Aryabhatta', 'Aryabhatta'), ('Ramanujan', 'Ramanujan'), ('C.V Raman', 'C.V Raman'),
            ('Mandakini', 'Mandakini'))

    fl = (('none', 'select'), ('ground', 'ground'), ('first', 'first'), ('second', 'second'), ('third', 'third'))

    rm = (('none', 'select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
          ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'),
          ('15', '15'), ('16', '16'))

    student_name = forms.CharField(max_length=30, label='Name')
    userid = forms.CharField(max_length=10)
    hostel = forms.ChoiceField(choices=host, initial='none')
    floor = forms.ChoiceField(choices=fl)
    room = forms.ChoiceField(choices=rm)
    appliances = forms.ChoiceField(choices=objects)
    status = forms.CharField(initial='pending', disabled=True)