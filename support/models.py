from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Ticket model
class Ticket(models.Model):
    STATUS_OPTIONS = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    ticket_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            now = datetime.now()
            # Generate ticket+_id as TT-YYYYMMDD-NNN(NNN is a three digit number)
            today_tickets_count = Ticket.objectsfilter(created_at__date=now.date()).count() + 1
            self.ticket_id = f"TT-{now.year}-{now.month:02d}{now.day:02d}-{today_tickets_count:03d}"
        super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.ticket_id


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.comment

