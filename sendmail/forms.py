from django import forms
from django.core.mail import EmailMessage
from decouple import config
from django.core.exceptions import ValidationError


class Contact_form(forms.Form):

    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'name'
        }))
    
    email = forms.EmailField(
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your best email',
            'class': 'email'
        }))

    subject = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'subject'
        }))

    message = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message',
            'class': 'message'
        }))
 
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        message1 = f"{name.capitalize()}: {email.lower()}\n\n\n{message.capitalize()}"

        mail = EmailMessage(
            to = [config('EMAIL_TARGET'), ],
            subject = subject.capitalize(),
            body = message1,
        )

        message_copy = f"You sent a message to Julio Kozarewicz:\n\n{'-' * 30}\nSubject: {subject.capitalize()}\n\n{message.capitalize()}\n{'-' * 30}\n\nWe will contact you =)"

        mail_copy = EmailMessage(
            to = [email.lower(), ],
            subject = f"COPY - {subject.capitalize()}",
            body = message_copy,
        )

        mail.send()
        mail_copy.send()

    def clean_name(self):

        super(Contact_form, self).clean()

        name = self.cleaned_data['name']

        if name.lower() == 'test':
            raise ValidationError('Name cannot be "test".')
        
        else:
            return name

    def clean_email(self):

        super(Contact_form, self).clean()

        email = self.cleaned_data['email']

        if email.lower() == 'test@email.com':
            raise ValidationError('Email cannot be "test@email.com".')
        
        if email.lower() == 'test@test.com':
            raise ValidationError('Email cannot be "test@test.com".')
        
        else:
            return email

    def clean_subject(self):

        super(Contact_form, self).clean()

        subject = self.cleaned_data['subject']

        if subject.lower() == 'test':
            raise ValidationError('Subject cannot be "test".')
        
        else:
            return subject