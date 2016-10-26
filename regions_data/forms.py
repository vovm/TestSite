from django import forms

from .models import Parse, Region


class ParseForm(forms.ModelForm):

    class Meta:
        model = Parse
        fields = ('file_name',)


class ShowForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Region.objects.all().order_by('name'),
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Choose a region')
