from django.forms import ModelForm
from department.models import Department


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        exclude = ['date_created', 'date_modified']