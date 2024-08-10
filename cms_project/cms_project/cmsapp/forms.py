from django import forms
from .models import AddModel
from .models import UploadModel
from .models import PollModel
from .models import AnotesModel

class PollForm(forms.ModelForm):
	class Meta:
		model = PollModel
		fields = ["question","op1","op2","op3"]
		widgets = {"question":forms.Textarea(attrs={'rows':4})}

class AddForm(forms.ModelForm):
	class Meta:
		model = AddModel
		fields = "__all__"

class AnotesForm(forms.ModelForm):
	class Meta:
		model = AnotesModel
		fields = "__all__"


class UploadForm(forms.ModelForm):
	class Meta:
		model = UploadModel
		fields = "__all__"
