from django.shortcuts import render, get_list_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Ticket

# Create your views here.
class TicketList(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "ticket_list.html"


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(reuest, 'support/create_ticket.html'), {'form': form}




