from django import forms
class Lab(forms.Form):
    lab=(('none', 'select'), ('CC','CC'), ('CL-1', 'CL-1'), ('CL-2','CL-2'), ('LIBRARY', 'lIBRARY'))
    prb=(('none', 'select'), ('Software', 'Software'), ('Mouse', 'Mouse'), ('Keyboard', 'Keyboard'), ('Monitor', 'Monitor'),
         )
    lab = forms.ChoiceField(choices=lab)
    system = forms.IntegerField(max_value=50, min_value=1)
    problem = forms.ChoiceField(choices=prb)
    lab_status = forms.CharField(initial='pending', disabled=True)

