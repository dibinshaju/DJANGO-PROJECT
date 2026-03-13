from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model=Student
        #we specify the fields we want to include in the form, if we want all fields we can use '_all_'
        fields=['first_name','last_name','email','courses']
        
        #we can also specify widgets to customize the form fields, for example to make the course field a multi-select dropdown
        widgets={
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Name'
                }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
                }),
            'courses':forms.CheckboxSelectMultiple()#change default multi select to checkbox
        }
    def clean_email(self):
        email=self.cleaned_data.get('email')
        
        if not email.endswith('@university.edu'):
            raise forms.ValidationError("Only university email addresses are allowed.")
        return email