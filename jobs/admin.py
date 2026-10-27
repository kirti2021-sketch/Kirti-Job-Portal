from django.contrib import admin

from .models import Job, Application, ContactMessage


# ================= JOB ADMIN =================

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'company',
        'location',
        'salary',
        'created_at'
    )

    search_fields = (
        'title',
        'company',
        'location'
    )


# ================= APPLICATION ADMIN =================

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'job',
        'email',
        'phone',
        'status',
        'applied_at'
    )

    list_filter = (
        'status',
        'applied_at'
    )

    search_fields = (
        'name',
        'email',
        'job__title'
    )


# ================= CONTACT MESSAGE ADMIN =================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'created_at'
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'subject',
        'message'
    )

    readonly_fields = (
        'created_at',
    )