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
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Invalid username or password')
    
    return render(request, 'account/login.html')