from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    title=forms.CharField(max_length=150, label='Malumot',
                          widget=forms.TextInput(attrs={"class": "form-control"}))
    context=forms.CharField(label='Teks',required=False,widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":5
    }))
    is_bool=forms.BooleanField(label='malumot?',initial=True)
    category=forms.ModelChoiceField(empty_label='Category tanlang',
                                    label='Category',queryset=Student.objects.all(),
                                    widget=forms.Select(attrs={"class": "form-control"}))

class FanlarForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label='Malumot',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    #
    # class Meta:
    #     model=Student
    #     fi

