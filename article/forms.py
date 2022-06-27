from django import forms

from article.models import Member


class MemberForm(forms.ModelForm):
	email = forms.CharField(widget=forms.EmailInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Enter your e-mail address'
		       }
	), label='')

	class Meta:
		model = Member
		fields = ('email', )
