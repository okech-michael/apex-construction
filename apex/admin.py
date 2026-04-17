from django.contrib import admin
from .models import Service, Project, TeamMember, Testimonial, MachineHire, ContactMessage, ConsultationBooking


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'location', 'year', 'is_featured', 'order']
    list_editable = ['status', 'is_featured', 'order']
    list_filter = ['status', 'is_featured']
    search_fields = ['title', 'description']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'role']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_role', 'client_company', 'rating', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['rating', 'is_active']


@admin.register(MachineHire)
class MachineHireAdmin(admin.ModelAdmin):
    list_display = ['name', 'rate', 'is_available', 'order']
    list_editable = ['is_available', 'order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']

    def has_add_permission(self, request):
        return False


@admin.register(ConsultationBooking)
class ConsultationBookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'preferred_date', 'preferred_time', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status', 'preferred_date']
    search_fields = ['name', 'email', 'phone']


# Customize admin site headers
admin.site.site_header = "Apex Construction Admin"
admin.site.site_title = "Apex Construction"
admin.site.index_title = "Welcome to Apex Construction Admin Panel"