from django.urls import path, include
from . import views
from .views import (

    EmailGroupCreateView,
    EmailGroupUpdateView,
    EmailGroupDeleteView,
    EmailGroupDetailView,
    email_group_detail_create,
    EmailGroupDetailUpdateView,
    EmailGroupDetailDeleteView,
)

urlpatterns = [
    path("", views.index_view, name="Login"),
    path("login/", views.login_view, name="Login"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),

    path("admin_dashboard/mail_log/", views.mail_log, name="mail_log"),
    path("admin_dashboard/remainder/", views.remainder, name="remainder"),
    path("admin_dashboard/tasks/", views.tasks, name="tasks"),

    path("admin_dashboard/email_group/", views.email_group, name="email_group"),

    path('groups/create/', EmailGroupCreateView.as_view(), name='email_group_create'),
    path('groups/<int:pk>/edit/', EmailGroupUpdateView.as_view(), name='email_group_update'),
    path('groups/<int:pk>/delete/', EmailGroupDeleteView.as_view(), name='email_group_delete'),
    path('groups/<int:pk>/', EmailGroupDetailView.as_view(), name='email_group_detail'),

    # EmailGroupDetails URLs
    path('groups/<int:group_id>/details/create/', email_group_detail_create, name='email_group_detail_create'),
    path('details/<int:pk>/edit/', EmailGroupDetailUpdateView.as_view(), name='email_group_detail_update'),
    path('details/<int:pk>/delete/', EmailGroupDetailDeleteView.as_view(), name='email_group_detail_delete'),
    path("admin_dashboard/email_group/create", views.email_group, name="create_mail_group"),




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
        "admin_dashboard/update_task/<int:id>/", views.update_task, name="update_task"
    ),
    path("delete_task/<int:id>/", views.delete_task, name="delete_task"),
]
