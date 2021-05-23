from django import forms


class EntryForm(forms.Form):
    author = forms.CharField(label='author', max_length=50, required=True)
    executor = forms.CharField(label='executor', max_length=50, required=True)

    granted_at = forms.CharField(label='granted_at', required=True)
    expired_at = forms.CharField(label='expired_at', required=True)

    resource = forms.CharField(label='resource', max_length=50, required=True)
    status = forms.CharField(label='status', max_length=50, required=True)


class FilterForm(forms.Form):
    author = forms.CharField(label='author', max_length=50, required=False)
    executor = forms.CharField(label='executor', max_length=50, required=False)

    granted_at = forms.CharField(label='granted_at', required=True)
    expired_at = forms.CharField(label='expired_at', required=True)

    resource = forms.CharField(label='resource', max_length=50, required=False)
