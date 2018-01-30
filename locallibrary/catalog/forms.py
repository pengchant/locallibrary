from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

from django.forms import ModelForm
from .models import BookInstance

class RenewBoolModelForm(ModelForm):
    '''
    Model form 的使用
    '''
    def clean_due_back(self):
        data = self.cleaned_data['due_back']
        if data<datetime.date.today():
            raise ValidationError(_('错误的时间 - 过去的时间'))
        
        if data>datetime.date.today+datetime.timedelta(weeks=3):
            raise ValidationError(_('错误的日期 - 不能超过4星期'))
        return data
    
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back':_('更新日期:')}
        help_text = {
            'due_back':_('输入一个日期从现在到未来4周之内')
        }

class RenewBookForm(forms.Form):
    '''
    修改bookinstance的表格
    '''
    renewal_date = forms.DateField(label="日期:",
        widget=forms.DateInput(attrs={
            'class':'form-control',
            'style':'width:300px',
            'placeholder':'输入一个日期在未来4周之内,默认为三周',
    }))
   
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('不合法的日期 - 过去的时间'))

        if data > datetime.date.today() + datetime.timedelta(weeks = 4):
            raise ValidationError(_('不合法的日期 - 超过了四周的时间'))

        # 返回日期
        return data