from django.contrib import admin
from .models import Information, Home, Specialize_data, Specialize_section,  Process_section, About,  Award_section, Skills_section, Logo_section, Testimonials_section, Work, Contact

#######################################################
                    #### HOME PAGE ADMIN ####
class DataAdmin(admin.StackedInline):
    model = Specialize_data
class SpecializeAdmin(admin.StackedInline):
    model = Specialize_section
class ProcessAdmin(admin.StackedInline):
    model = Process_section
    

class HomeAdmin(admin.ModelAdmin):
  list_display = ('no_of_visted', 'no_of_views')
  fieldsets = (
        ('First Section', {
            "fields": (
                'header_content', 'specialize_content', 'showcase_image'
            ),
        }),
        ('Second Section', {
            "classes": ('collapse',),
            "fields": (
                'specialist_title', 'specialist_summary'
            ),
        }),
        ('Third Section', {
            "classes": ('collapse',),
            "fields": (
                'client', 'award', 'hours_worked', 'project_completed'
            ),
        }),
        ('Fourth Section', {
            "classes": ('collapse',),
            "fields": (
                'section_title', 'section_content'
            ),
        }),
    )
  inlines = [DataAdmin, SpecializeAdmin, ProcessAdmin]

###################################################################

#########About page admin###############

class AwardAdmin(admin.StackedInline):
    model = Award_section
class SkillAdmin(admin.StackedInline):
    model = Skills_section
class LogoAdmin(admin.StackedInline):
    model = Logo_section
class TestimonialAdmin(admin.StackedInline):
    model = Testimonials_section


class AboutAdmin(admin.ModelAdmin):
    list_display = ('no_of_visted', 'no_of_views')
    fieldsets = (
        ('Body Content', {
            "fields": (
                'heading', 'title', 'details', 'image'
            ),
        }),
        ('Information', {
            "classes": ('collapse',),
            "fields": (
                'no_of_visted', 'no_of_views'
            ),
        }),
    )
    inlines = [AwardAdmin, SkillAdmin, LogoAdmin, TestimonialAdmin]

class WorkAdmin(admin.ModelAdmin):
    
  list_display = ('title','no_of_visted', 'no_of_views')
  search_fields = ('title', 'description',)
  fieldsets = (

    ('', {
            "fields": (
                'title', 'video', 'image', 'description', 'github_link',
            ),
        }),
        ('user activeness', {
            "classes": ('collapse',),
            "fields": (
                'no_of_visted', 'no_of_views'
            ),
    }),
 )

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'subject','no_of_visted', 'no_of_views')
  search_fields = ('name', 'email', 'phone',)
  fieldsets = (
    ('', {
            "fields": (
                'name', 'email', 'subject', 'phone', 'message', 'sent_date',
            ),
        }),
        ('user activeness', {
            "fields": (
                'no_of_visted', 'no_of_views'
            ),
    }),
 )

class InfoAdmin(admin.ModelAdmin):
    list_display = ('country', 'Ip_address','device_type',)
    search_fields = ('country', 'Ip_address', 'device_type',)

admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Information, InfoAdmin)
