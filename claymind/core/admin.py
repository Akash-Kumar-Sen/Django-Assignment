from django.contrib import admin
from core.admin_export_resources import PersonDataResource
from core.models import PersonData
from import_export.admin import ExportMixin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

@admin.register(PersonData)
class PersonDataAdmin(ExportMixin, SafeDeleteAdmin):
    """
    Admin definition for the User model
    """
    resource_class = PersonDataResource
    list_display = (highlight_deleted, 'id', 'name', 'email', 'phone', 'contact',
                    'created_at', 'modified_at',) + SafeDeleteAdmin.list_display
    list_per_page = 25
    readonly_fields = ('created_at', 'modified_at', 'deleted')
    ordering = ('order_value',)
