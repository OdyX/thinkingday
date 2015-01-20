from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from allauth.account.forms import BaseSignupForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.models import SocialAccount


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


class SocAccountChoiceField(forms.ModelChoiceField):
    user = False

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        kwargs['queryset'] = SocialAccount.objects.filter(user=self.user)
        super(SocAccountChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return "{provider} ({account})".format(
            provider=obj.provider.title(),
            account=obj.get_provider_account())


class ProfileForm(forms.ModelForm):
    scoutname = forms.CharField(max_length=512)
    socialaccount = SocAccountChoiceField(
        required=False,
        user=False)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        if SocialAccount.objects.filter(user=kwargs['instance']).count() > 0:
            self.fields['socialaccount'] = \
                     SocAccountChoiceField(
                        label=_('Preferred social account'),
                        required=False,
                        user=kwargs['instance'])

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'scoutname', 'socialaccount']

    def as_divs(self):
        "Returns this form rendered as <div>s."
        return self._html_output(
            normal_row=u'<div class="pure-control-group">' +
                       '%(errors)s%(label)s%(field)s%(help_text)s' +
                       '</div>',
            error_row='<div>%s</div>',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=False)