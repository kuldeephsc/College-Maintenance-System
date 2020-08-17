from django import forms
class IToutpass(forms.Form):
    year = (('none','select'), ('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'final'))
    it_name = forms.CharField(max_length=30, label='Name')
    it_rollnumber = forms.CharField(max_length=10, label='Roll Number')
    it_year = forms.ChoiceField(choices=year, label='year')
    it_branch = forms.CharField(max_length=2, label='Branch', initial='IT', disabled=True)
    it_reason = forms.CharField(widget=forms.Textarea(), label='Reason')
    it_start_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='From')
    it_end_date = forms.DateField(widget=forms.SelectDateWidget(years=['2020']), label='To')
    it_permission = forms.CharField(max_length=10, initial='requested', disabled=True, label='Status')