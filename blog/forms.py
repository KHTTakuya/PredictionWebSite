from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label="件名")
    email = forms.EmailField(label='Email', help_text="※ご確認の上、正しく入力してください。")
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)