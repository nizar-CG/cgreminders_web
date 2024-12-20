from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .form import (
    RemainderTypesForm,

    TasksForm,
    MailLogForm,
)
from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import EmailGroups, EmailGroupDetails
from .form import EmailGroupForm, EmailGroupDetailForm


def index_view(request):
    #check if the user is authenticated
    if request.user.is_authenticated:
        return redirect('/admin_dashboard')
    else:
        return redirect("/login")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('/admin/')
            elif not request.user.is_superuser:
                return redirect('/admin_dashboard/')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
def email_group(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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

# --- EmailGroups Views ---



# Create View for EmailGroups
class EmailGroupCreateView(CreateView):
    model = EmailGroups
    form_class = EmailGroupForm
    template_name = "email_group_form.html"
    success_url = reverse_lazy('email_group')

# Update View for EmailGroups
class EmailGroupUpdateView(UpdateView):
    model = EmailGroups
    form_class = EmailGroupForm
    template_name = "email_group_form.html"
    success_url = reverse_lazy('email_group')

# Delete View for EmailGroups
class EmailGroupDeleteView(DeleteView):
    model = EmailGroups
    template_name = "email_group_confirm_delete.html"
    success_url = reverse_lazy('email_group')

# Detail View for EmailGroups
class EmailGroupDetailView(DetailView):
    model = EmailGroups
    template_name = "email_group_detail.html"
    context_object_name = "group"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add related EmailGroupDetails to the context
        context['details'] = self.object.details.all()
        return context

# --- EmailGroupDetails Views ---

# Create View for EmailGroupDetails
def email_group_detail_create(request, group_id):
    group = get_object_or_404(EmailGroups, id=group_id)

    if request.method == 'POST':
        form = EmailGroupDetailForm(request.POST, group=group)
        if form.is_valid():
            # Save the form with the group_detail
            group_detail = form.save(commit=False)
            # Ensure the ForeignKey is properly set
            group_detail.group_detail = group  # Explicitly set the group_detail ForeignKey
            group_detail.save()
            return redirect('email_group_detail', group.id)  # Redirect to detail page
    else:
        form = EmailGroupDetailForm(group=group)

    return render(request, 'email_group_detail_form.html', {'form': form, 'group': group})

# Update View for EmailGroupDetails
class EmailGroupDetailUpdateView(UpdateView):
    model = EmailGroupDetails
    form_class = EmailGroupDetailForm
    template_name = "email_group_detail_form.html"

    def get_success_url(self):
        return reverse_lazy('email_group_detail', self.object.group_detail.id)

# Delete View for EmailGroupDetails
class EmailGroupDetailDeleteView(DeleteView):
    model = EmailGroupDetails
    template_name = "email_group_detail_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('email_group_detail', kwargs={'pk': self.object.group_detail.id})
def mail_log(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        remainder_types = RemainderTypes.objects.all()
        email_groups = EmailGroups.objects.all()
        email_group_details = EmailGroupDetails.objects.all()
        if not request.user.is_superuser:
            tasks = Tasks.objects.filter(user=request.user)
        else:
            tasks = Tasks.objects.all()
        mail_logs = MailLog.objects.all()

        context = {
            "remainder_types": remainder_types,
            "email_groups": email_groups,
            "email_group_details": email_group_details,
            "tasks": tasks,
            "mail_logs": mail_logs,
            'form': TasksForm,
        }
        return render(request, "tasks.html", context)





def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if request.method == "POST":
            form = RemainderTypesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("remainder")
        else:
            form = RemainderTypesForm()
        return render(request, "remainder.html", {"form": form})








def tasks_create(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if request.method == "POST":
            form = TasksForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)  # Don't save to DB yet
                task.user = request.user  # Set the current user
                task.state = "unsend"  # Set state to "send"
                task.save()
            return redirect("tasks")
        else:
            form = TasksForm()
        return render(request, "tasks.html", {"form": form})


def mail_log_create(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if request.method == "POST":
            form = MailLogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("mail_log")
        else:
            form = MailLogForm()
        return render(request, "mail_log.html", {"form": form})


def update_remainder_type(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        remainder = get_object_or_404(RemainderTypes, id=id)
        remainder.delete()
        return redirect("remainder")


def update_mail_log(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        mail_log = get_object_or_404(MailLog, id=id)
        mail_log.delete()
        return redirect("mail_log")










def update_task(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
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
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        task = get_object_or_404(Tasks, id=id)
        task.delete()
        return redirect("tasks")
