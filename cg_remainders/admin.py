from django.contrib import admin
from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog


# Enregistrer le modèle RemainderTypes
@admin.register(RemainderTypes)
class RemainderTypesAdmin(admin.ModelAdmin):
    list_display = ("label", "before_duration", "remainder_frequency")
    search_fields = ("label",)
    list_filter = ("remainder_frequency",)


# Enregistrer le modèle EmailGroups
@admin.register(EmailGroups)
class EmailGroupsAdmin(admin.ModelAdmin):
    list_display = ("group_name",)
    search_fields = ("group_name",)


# Enregistrer le modèle EmailGroupDetails
@admin.register(EmailGroupDetails)
class EmailGroupDetailsAdmin(admin.ModelAdmin):
    list_display = ("email", "group_detail")
    search_fields = ("email",)
    list_filter = ("group_detail",)


# Enregistrer le modèle Tasks
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("description", "state", "mailgroup", "remaindertype")
    search_fields = ("description",)
    list_filter = ("state", "remaindertype", "mailgroup")


# Enregistrer le modèle MailLog
@admin.register(MailLog)
class MailLogAdmin(admin.ModelAdmin):
    list_display = ("description", "dateofsend", "email_group")
    search_fields = ("description",)
    list_filter = ("dateofsend",)
