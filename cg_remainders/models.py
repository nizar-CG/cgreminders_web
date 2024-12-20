from django.db import models
from django.contrib.auth.models import User


# RemainderTypes
class RemainderTypes(models.Model):
    label = models.CharField(max_length=100)
    before_duration = models.IntegerField()
    remainder_frequency = models.IntegerField()

    def __str__(self):
        return self.label




class EmailGroups(models.Model):
    group_name = models.CharField(max_length=200, verbose_name="Group Name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "Email Group"
        verbose_name_plural = "Email Groups"


class EmailGroupDetails(models.Model):
    email = models.EmailField(verbose_name="Email")
    group_detail = models.ForeignKey(
        EmailGroups, on_delete=models.CASCADE, related_name="details", verbose_name="Group"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email Group Detail"
        verbose_name_plural = "Email Group Details"

# Tasks
class Tasks(models.Model):
    STATE_CHOICES = [
        ("unsend", "Unsend"),
        ("send", "Send"),
        ("under_frequency", "Under Frequency"),
    ]

    description = models.TextField()
    main_object = models.TextField()
    remaindertype = models.ForeignKey(RemainderTypes, on_delete=models.CASCADE)
    mailgroup = models.ForeignKey(EmailGroups, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="unsend")
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")  # Link to User


    def __str__(self):
        return self.description


# MailLog
class MailLog(models.Model):
    description = models.TextField()
    dateofsend = models.DateTimeField()
    email_group = models.OneToOneField(EmailGroups, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mail sent on {self.dateofsend}"
