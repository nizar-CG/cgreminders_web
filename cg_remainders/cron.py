from django.core.mail import send_mail

from .models import Tasks,RemainderTypes,EmailGroups,MailLog,EmailGroupDetails
from datetime import datetime , timedelta
def my_scheduled_job():
  today = datetime.now().date()
  tasks = Tasks.objects.all()
  print('mail checking')

  for task in tasks:
      send_factor = (task.due_date - today).days
      print(send_factor,task.due_date, task.remaindertype.before_duration, task.description)
      #check by due date against send factor
      if send_factor == task.remaindertype.before_duration :

        l = []
        group_detils = EmailGroupDetails.objects.filter(group_detail=task.mailgroup.id)
        for group in group_detils:
          l.append(group.email)
        print(task.mailgroup.details,l)
        send_mail(
          task.main_object,
          task.description,
          'cgreminder@carthageit.com',
          l,
          fail_silently=False,
        )
        print('mail sent')
        mail_log_object = MailLog.objects.create(description=task.main_object,date=today,email_group=task.mailgroup.group_name)
        task.state = 'send'
      if send_factor < task.remaindertype.before_duration and (send_factor / task.remaindertype.remainder_frequency) == 0 :
        send_mail(
          'Reminder of a sent notification {0}'.format(task.main_object),
          task.description,
          'cgreminder@carthageit.com',
          task.mailgroup.details,
          fail_silently=False,
        )
        mail_log_object = MailLog.objects.create(description='Reminder of a sent notification {0}'.format(task.main_object), date=today,
                                                 email_group=task.mailgroup.group_name)
        task.state = 'under_frequency'
