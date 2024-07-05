from django.shortcuts import render, get_list_or_404
from django.views import generic
from .models import Ticket
from .forms import UserForm

# Create your views here.
class TicketList(generic.ListView):
    queryset = Ticket.objects.all()
    template_name = "ticket_list.html"


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'support/register.html', {'form': form})