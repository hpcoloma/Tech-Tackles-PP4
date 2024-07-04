from django.shortcuts import render
from django.views import generic
from .models import Ticket

# Create your views here.
class TicketList(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "ticket_list.html"
