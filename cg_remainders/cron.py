from django.core.mail import send_mail

from .models import Tasks,RemainderTypes,EmailGroups,MailLog
from datetime import datetime , timedelta
def my_scheduled_job():
  today = datetime.now().date()
  tasks = Tasks.objects.all()

  for task in tasks:
      send_factor = (task.due_date - today).days
      #check by due date against send factor
      if send_factor == task.remaindertype.before_duration :
        send_mail(
          task.main_object,
          task.description,
          'cgreminder@carthageit.com',
          task.mailgroup.details,
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
