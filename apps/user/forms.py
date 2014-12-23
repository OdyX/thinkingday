from django import forms
from allauth.account.forms import BaseSignupForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class EmailOnlyForm(BaseSignupForm):
    confirmation_key = forms.CharField(max_length=40,
                                       required=False,
                                       widget=forms.HiddenInput())

    #def __init__(self, *args, **kwargs):
        #super(EmailOnlyForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(EmailOnlyForm, self).clean()
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        # Enforce the username to be the email
        self.cleaned_data['username'] = \
            self.cleaned_data['email']
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user