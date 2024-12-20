from django.db import models


# RemainderTypes
class RemainderTypes(models.Model):
    label = models.CharField(max_length=100)
    before_duration = models.IntegerField()
    remainder_frequency = models.IntegerField()

    def __str__(self):
        return self.label


# EmailGroupDetails
class EmailGroupDetails(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


# EmailGroups
class EmailGroups(models.Model):
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name


# EmailGroupDetails
class EmailGroupDetails(models.Model):
    email = models.EmailField()
    group_detail = models.ForeignKey(
        "EmailGroups", on_delete=models.CASCADE, related_name="groupdetails"
    )

    def __str__(self):
        return self.email


# Tasks
class Tasks(models.Model):
    STATE_CHOICES = [
        ("unsend", "Unsend"),
        ("send", "Send"),
        ("under_frequency", "Under Frequency"),
    ]

    description = models.TextField()
    remaindertype = models.ForeignKey(RemainderTypes, on_delete=models.CASCADE)
    mailgroup = models.ForeignKey(EmailGroups, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)

    def __str__(self):
        return self.description


# MailLog
class MailLog(models.Model):
    description = models.TextField()
    dateofsend = models.DateTimeField()
    email_group = models.OneToOneField(EmailGroups, on_delete=models.CASCADE)

    def __str__(self):
        return f"Mail sent on {self.dateofsend}"
