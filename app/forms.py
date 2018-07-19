from django import forms
from .models import Student,ramkrishna,delete


class Stuform(forms.ModelForm):
      class Meta:
          model = Student
          fields = ['Name','Mobile','Email','password','Gender','City','State']
class logform(forms.ModelForm):
      class Meta:
          model = ramkrishna
          fields=['Email','password']

class deleteform(forms.ModelForm):
    class Meta:
        model = delete
        fields = ['Email']