from django import forms
from .models import hostinfo
class UserForm(forms.Form):
    username = forms.CharField(label='',max_length=100,widget=forms.TextInput(
        attrs={'id': 'username','placeholder': 'User'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(
        attrs={'id': 'password','placeholder': 'Password'}))

class autoArrMinionForm(forms.Form):
    add_hostname = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'id': 'add_minion_hostname', 'placeholder': 'hostname', 'class': 'form-control'}))
    add_ip = forms.GenericIPAddressField(label='add_minion_ip',max_length=50,widget=forms.TextInput(
        attrs={'id':'add_minion_ip','name':'add_minion_ip','placeholder':'IP','class':'form-control'}))
    add_username = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'id': 'add_minion_username', 'placeholder': 'Hot_user', 'class': 'form-control'}))
    add_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'id': 'add_minion_password', 'placeholder': 'Password', 'class': 'form-control'}))
    add_port = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'id': 'add_minion_port', 'placeholder': 'Port', 'class': 'form-control'}))
    add_outport = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'id': 'add_minion_outport', 'placeholder': 'Out_port', 'class': 'form-control'}))
    add_work_dir = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'id': 'add_minion_work_dir', 'placeholder': 'Work_dir', 'class': 'form-control'}))
