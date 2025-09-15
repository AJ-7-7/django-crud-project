from django import forms
from .models import EmployeeData,Jobs

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = '__all__'
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['jobid'].queryset = Jobs.objects.all()  # Populate dropdown with Jobs queryset
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        widgets = {
            # Define widgets if needed for Jobs model fields
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.required = True