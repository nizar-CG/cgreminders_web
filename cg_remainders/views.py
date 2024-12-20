from django.shortcuts import render, get_object_or_404, redirect
from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog
from .form import (
    RemainderTypesForm,
    EmailGroupsForm,
    EmailGroupDetailsForm,
    TasksForm,
    MailLogForm,
)
from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog


def index_view(request):
    return render(request, "index.html")


def email_group(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "email_group.html", context)


def mail_log(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "mail_log.html", context)


def remainder(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "remainder.html", context)


def tasks(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "tasks.html", context)


def email_group_detail(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "email_group_detail.html", context)


def admin_dashboard(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        "remainder_types": remainder_types,
        "email_groups": email_groups,
        "email_group_details": email_group_details,
        "tasks": tasks,
        "mail_logs": mail_logs,
    }
    return render(request, "admin_dashboard.html", context)


def remainder_types_create(request):
    if request.method == "POST":
        form = RemainderTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("remainder")
    else:
        form = RemainderTypesForm()
    return render(request, "remainder.html", {"form": form})


def email_groups_create(request):
    if request.method == "POST":
        form = EmailGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("email_group")
    else:
        form = EmailGroupsForm()
    return render(request, "email_group.html", {"form": form})


def emails_groups_create(request):
    if request.method == "POST":
        form = EmailGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("email_group_detail")
    else:
        form = EmailGroupsForm()
    return render(request, "email_group_detail.html", {"form": form})


def email_group_details_create(request):

    if request.method == "POST":
        form = EmailGroupDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("email_group_detail")
    else:
        form = EmailGroupDetailsForm()
    return render(request, "email_group_detail.html", {"form": form})


def tasks_create(request):
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = TasksForm()
    return render(request, "tasks.html", {"form": form})


def mail_log_create(request):
    if request.method == "POST":
        form = MailLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mail_log")
    else:
        form = MailLogForm()
    return render(request, "mail_log.html", {"form": form})


def update_remainder_type(request, id):
    remainder = get_object_or_404(RemainderTypes, id=id)

    if request.method == "POST":
        form = RemainderTypesForm(request.POST, instance=remainder)
        if form.is_valid():
            form.save()
            return redirect("remainder")
    else:
        form = RemainderTypesForm(instance=remainder)

    return render(
        request, "remainder_update.html", {"form": form, "remainder": remainder}
    )


def delete_remainder_type(request, id):
    remainder = get_object_or_404(RemainderTypes, id=id)
    remainder.delete()
    return redirect("remainder")


def update_mail_log(request, id):
    mail_log = get_object_or_404(MailLog, id=id)

    if request.method == "POST":
        form = MailLogForm(request.POST, instance=mail_log)
        if form.is_valid():
            form.save()
            return redirect("mail_log")
    else:
        form = MailLogForm(instance=mail_log)

    return render(request, "mail_log_update.html", {"form": form, "mail_log": mail_log})


def delete_mail_log(request, id):
    mail_log = get_object_or_404(MailLog, id=id)
    mail_log.delete()
    return redirect("mail_log")


def update_email_group(request, id):
    group = get_object_or_404(EmailGroups, id=id)

    if request.method == "POST":
        form = EmailGroupsForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("email_group")
    else:
        form = EmailGroupsForm(instance=group)

    return render(request, "email_group_update.html", {"form": form, "group": group})


def delete_email_group(request, id):
    group = get_object_or_404(EmailGroups, id=id)
    group.delete()
    return redirect("email_group")


def update_email_group_detail(request, id):
    detail = get_object_or_404(EmailGroupDetails, id=id)
    email_groups = EmailGroups.objects.all()

    if request.method == "POST":
        form = EmailGroupDetailsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect("email_group_detail")
    else:
        form = EmailGroupDetailsForm(instance=detail)

    return render(
        request,
        "email_group_detail_update.html",
        {"form": form, "detail": detail, "email_groups": email_groups},
    )


def delete_email_group_detail(request, id):
    detail = get_object_or_404(EmailGroupDetails, id=id)
    detail.delete()
    return redirect("email_group_detail")


def update_task(request, id):
    task = get_object_or_404(Tasks, id=id)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = TasksForm(instance=task)

    return render(request, "tasks_update.html", {"form": form, "task": task})


def delete_task(request, id):
    task = get_object_or_404(Tasks, id=id)
    task.delete()
    return redirect("tasks")
