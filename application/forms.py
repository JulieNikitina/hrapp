from django import forms
from django.forms import DateField

from hr_app import settings
from .models import Record


class AddRecordForm(forms.ModelForm):
    interview_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Record
        fields = [
            'applicant_name',
            'phone_number',
            'position',
            'department',
            'interview_date',
            'time_to_complete',
            'name_hr',
            'position_hr',
        ]


class EditRecordByHeadOfDepartment(forms.ModelForm):
    date_of_get = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Record
        fields = [
            'date_of_get',
            'head_of_department_name'
        ]