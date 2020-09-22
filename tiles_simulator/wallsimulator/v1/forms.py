import csv
import codecs
from django import forms
from wallsimulator.v1.services import new_design_create_service



class NewDesignCreateForm(forms.Form):
    tile_number = forms.CharField(max_length=128)
    light = forms.ImageField()
    high_lighter_1 = forms.ImageField()
    high_lighter_2 = forms.ImageField(required=False, allow_empty_file=True)
    high_lighter_3 = forms.ImageField(required=False, allow_empty_file=True)
    dark = forms.ImageField()

    def perform_task_and_get_data(self):
        creation_id = new_design_create_service.CreateNewDesign(self.cleaned_data).create()
        print(creation_id)