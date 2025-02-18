# This file is where we'll list our blog app-specific URLs.
from . import views
from django.urls import path

urlpatterns = [
    path('', views.TicketList.as_view(), name='home'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('<int:ticket_id/', views.ticket_detail, name='ticket_detail')
]