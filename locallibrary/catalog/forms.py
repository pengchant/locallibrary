from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='输入一个日期在未来4周之内,默认为三周')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('不合法的日期 - 过去的时间'))

        if data > datetime.date.today() + datetime.timedelta(weeks = 4):
            raise ValidationError(_('不合法的日期 - 超过了四周的时间'))

        # 返回日期
        return data