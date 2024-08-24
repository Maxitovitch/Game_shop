from .models import SupportTicket
from django import forms


class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['subject', 'email', 'message']





