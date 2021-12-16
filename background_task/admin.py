# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import timezone
from background_task.models import Task
from background_task.models import CompletedTask


def inc_priority(modeladmin, request, queryset):
    for task in queryset:
        task.priority += 1
        task.save(update_fields=['priority'])
inc_priority.short_description = 'priority += 1'


def dec_priority(modeladmin, request, queryset):
    for task in queryset:
        task.priority -= 1
        task.save(update_fields=['priority'])
dec_priority.short_description = 'priority -= 1'


def run_now(modeladmin, request, queryset):
    for task in queryset:
        task.run_at = timezone.now()
        task.save(update_fields=['run_at'])
run_now.short_description = 'Run now'


class TaskAdmin(admin.ModelAdmin):
    display_filter = ['task_name']
    search_fields = ['task_name', 'task_params', 'task_hash']
    list_display = ['task_name', 'task_params', 'run_at', 'priority', 'attempts', 'has_error', 'locked_by', 'locked_by_pid_running', ]
    actions = [run_now, inc_priority, dec_priority]


class CompletedTaskAdmin(admin.ModelAdmin):
    display_filter = ['task_name']
    search_fields = ['task_name', 'task_params', 'task_hash']
    list_display = ['task_name', 'task_params', 'run_at', 'priority', 'attempts', 'has_error', 'locked_by', 'locked_by_pid_running', ]


admin.site.register(Task, TaskAdmin)
admin.site.register(CompletedTask, CompletedTaskAdmin)
