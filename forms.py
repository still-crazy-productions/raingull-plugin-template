from django import forms

class ExamplePluginConfigForm(forms.Form):
    service_name = forms.CharField(max_length=100, required=True)
    platform_server = forms.CharField(max_length=200, required=True)
    platform_port = forms.IntegerField(initial=443, required=True)
    encryption = forms.ChoiceField(choices=[("None","None"), ("STARTTLS","STARTTLS"), ("SSL/TLS","SSL/TLS")], required=True)
    platform_username = forms.CharField(required=False)
    platform_password = forms.CharField(widget=forms.PasswordInput, required=False)
    poll_frequency = forms.IntegerField(initial=5, required=False)