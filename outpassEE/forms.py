from django import forms
class EEoutpass(forms.Form):
    year = (('none','select'), ('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'final'))
    ee_name = forms.CharField(max_length=30, label='Name')
    ee_rollnumber = forms.CharField(max_length=10, label='Roll Number')
    ee_year = forms.ChoiceField(choices=year, label='year')
    ee_branch = forms.CharField(max_length=2, label='Branch', initial='EE', disabled=True)
    ee_reason = forms.CharField(widget=forms.Textarea(), label='Reason')
    ee_start_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='From')
    ee_end_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='To')
    ee_permission = forms.CharField(max_length=10, initial='requested', disabled=True, label='Status')