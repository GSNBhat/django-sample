from wsgiref.util import request_uri

from django import forms

domains = ['domain3000', 'domain4000', 'domain6000', 'domain7000']
projects = [('opscon','Opscon' ),('obestater', 'Obestater')]

domain = [(item, item) for item in domains]
domain.insert(0, ('', '--select--'))
#designation = [(item, item) for item in designation]
#designation.insert(0, ('', '--select--'))

class DeplymentForm(forms.Form):

    domain = forms.ChoiceField(label='Domain', choices=domain, required=True)
    project = forms.CharField(label='Which projects????', widget=forms.RadioSelect(choices=projects ))
    warName = forms.CharField(label='warName',max_length=100)
  #  project = forms.RadioSelect( choices=FRUIT_CHOICES)
