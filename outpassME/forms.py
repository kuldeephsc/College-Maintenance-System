from django import forms
class MEoutpass(forms.Form):
    year = (('none','select'), ('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'final'))
    me_name = forms.CharField(max_length=30, label='Name')
    me_rollnumber = forms.CharField(max_length=10, label='Roll Number')
    me_year = forms.ChoiceField(choices=year, label='year')
    me_branch = forms.CharField(max_length=2, label='Branch', initial='ME', disabled=True)
    me_reason = forms.CharField(widget=forms.Textarea(), label='Reason')
    me_start_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='From')
    me_end_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='To')
    me_permission = forms.CharField(max_length=10, initial='requested', disabled=True, label='Status')