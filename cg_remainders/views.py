from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")


from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog

def admin_dashboard(request):
    remainder_types = RemainderTypes.objects.all()
    email_groups = EmailGroups.objects.all()
    email_group_details = EmailGroupDetails.objects.all()
    tasks = Tasks.objects.all()
    mail_logs = MailLog.objects.all()

    context = {
        'remainder_types': remainder_types,
        'email_groups': email_groups,
        'email_group_details': email_group_details,
        'tasks': tasks,
        'mail_logs': mail_logs,
    }
    return render(request, 'admin_dashboard.html', context)