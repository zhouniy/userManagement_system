from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from web_management import models
from web_management.utils.bootstrap import BootstrapForm,BootstrapModelForm


class UserModelForm(BootstrapModelForm):
    class Meta:
        model = models.Userinfo
        fields = ["username", "password", "age", "account", "create_time", "depart", "gender"]


class PrettyModelForm(BootstrapModelForm):
    mobile = forms.CharField(
        label="手机号码",
        validators=[RegexValidator(r"^1[3-9]\d{9}$", "手机号格式错误")]
    )

    class Meta:
        model = models.PrettyInfo
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        txt = self.cleaned_data["mobile"]
        exists = models.PrettyInfo.objects.exclude(id=self.instance.pk).filter(mobile=txt).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt
