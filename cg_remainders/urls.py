from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index_view, name="Login"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin_dashboard/email_group/", views.email_group, name="email_group"),
    path("admin_dashboard/mail_log/", views.mail_log, name="mail_log"),
    path("admin_dashboard/remainder/", views.remainder, name="remainder"),
    path("admin_dashboard/tasks/", views.tasks, name="tasks"),
    path(
        "admin_dashboard/email_group_detail/",
        views.email_group_detail,
        name="email_group_detail",
    ),
    path("add_email_group/", views.email_groups_create, name="add_email_group"),
    path(
        "admin_dashboard/email_group_detail/",
        views.emails_groups_create,
        name="add_email_groups",
    ),
    path(
        "add_email_group_detail/",
        views.email_group_details_create,
        name="add_email_group_detail",
    ),
    path("add_mail_log/", views.mail_log_create, name="add_mail_log"),
    path(
        "add_remainder_type/", views.remainder_types_create, name="add_remainder_type"
    ),
    path("add_task/", views.tasks_create, name="add_task"),
    path(
        "admin_dashboard/update_remainder_type/<int:id>/",
        views.update_remainder_type,
        name="update_remainder_type",
    ),
    path(
        "delete_remainder_type/<int:id>/",
        views.delete_remainder_type,
        name="delete_remainder_type",
    ),
    path(
        "admin_dashboard/update_mail_log/<int:id>/",
        views.update_mail_log,
        name="update_mail_log",
    ),
    path("delete_mail_log/<int:id>/", views.delete_mail_log, name="delete_mail_log"),
    path(
        "admin_dashboard/update_email_group/<int:id>/",
        views.update_email_group,
        name="update_email_group",
    ),
    path(
        "delete_email_group/<int:id>/",
        views.delete_email_group,
        name="delete_email_group",
    ),
    path(
        "admin_dashboard/update_email_group_detail/<int:id>/",
        views.update_email_group_detail,
        name="update_email_group_detail",
    ),
    path(
        "delete_email_group_detail/<int:id>/",
        views.delete_email_group_detail,
        name="delete_email_group_detail",
    ),
    path(
        "admin_dashboard/update_task/<int:id>/", views.update_task, name="update_task"
    ),
    path("delete_task/<int:id>/", views.delete_task, name="delete_task"),
]
