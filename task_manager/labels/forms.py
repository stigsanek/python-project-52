from django.forms import ModelForm
from task_manager.labels.models import Label


class LabelForm(ModelForm):
    """Form for label creation and update"""

    class Meta:
        model = Label
        fields = ['name']
