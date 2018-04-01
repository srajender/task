from django import forms
class CustomerForm(forms.Form):
	account_number=forms.CharField(max_length=10,help_text='please enter account number')