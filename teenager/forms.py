from django.forms import ModelForm
from django import forms
from tempus_dominus.widgets import DatePicker
from .models import Student, Institution
from accounts.models import Profile
from django.contrib.auth.models import User

class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name', 'middle_name','date_of_birth','state_of_origin','sex','email_address', 
			'image', 'phone_number', 'parent_full_name', 'parent_phone_number', 'address',

		 ]

		widgets ={
			'date_of_birth': DatePicker( 
					options = {

					'minDate': '1998-01-01'
					}
				)

		}



class InstitutionCreateForm(ModelForm):
	class Meta:
		model = Institution
		fields = [ 'school', 'degree', 'field_of_study', 'grade_or_class', 'started', 'ended' ]	

		widgets = {
			'started': DatePicker(
				options={
				'minDate': '1998-01-01'
				}
				),


			'ended': DatePicker(
				options={'minDate': '1998-01-01'}

				)
		}


#form to update user profile on the profile display page.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


#form to to update user profile.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']