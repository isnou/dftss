from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

@admin.register(Book)
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='project/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "project"

    def __str__(self):
        return self.project_name

@admin.register(Book)
class Service(models.Model):
    service_title = models.CharField(max_length=50)
    service_description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='service/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.service_name

@admin.register(Book)
class Partner(models.Model):
    partner_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='partner/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "partner"

    def __str__(self):
        return self.partner_name

@admin.register(Book)
class Team(models.Model):
    member_name = models.CharField(max_length=50)
    member_function = models.TextField(max_length=100, blank=True)
    function_description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='team/', height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name = "team"

    def __str__(self):
        return self.team_name

@admin.register(Book)
class Counter(models.Model):
    counter_title = models.CharField(max_length=100)
    counter_value = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "counter"

    def __str__(self):
        return self.counter_name

@admin.register(Book)
class Content(models.Model):
    profile_name = models.CharField(max_length=50, blank=True)

    head_title = models.CharField(max_length=50)

    head_logo = models.ImageField(upload_to='content/head', height_field=None, width_field=None, max_length=100)
    main_logo = models.ImageField(upload_to='content/main', height_field=None, width_field=None, max_length=100)

    menu_bar_closed_title = models.CharField(max_length=20, blank=True)
    menu_bar_opened_title = models.CharField(max_length=20, blank=True)
    menu_bar_home = models.CharField(max_length=30)
    menu_bar_about = models.CharField(max_length=30)
    menu_bar_services = models.CharField(max_length=30)
    menu_bar_projects = models.CharField(max_length=30)
    menu_bar_partners = models.CharField(max_length=30)
    menu_bar_contact = models.CharField(max_length=30)

    intro_text = models.TextField(max_length=200, blank=True)

    intro_button = models.CharField(max_length=50)

    scroll_down_button = models.CharField(max_length=50)

    about_us_intro = models.CharField(max_length=200, blank=True)
    about_us_title = models.CharField(max_length=200, blank=True)
    about_us_description = models.TextField(max_length=500, blank=True)

    services_intro = models.CharField(max_length=200, blank=True)
    services_description = models.TextField(max_length=500, blank=True)

    projects_intro = models.CharField(max_length=200, blank=True)
    projects_description = models.TextField(max_length=500, blank=True)

    partners_intro = models.CharField(max_length=200, blank=True)
    partners_description = models.TextField(max_length=500, blank=True)

    contact_intro = models.CharField(max_length=200, blank=True)
    contact_description = models.TextField(max_length=500, blank=True)

    message_title = models.CharField(max_length=100, blank=True)
    message_name_placeholder = models.CharField(max_length=100, blank=True)
    message_email_placeholder = models.CharField(max_length=100, blank=True)
    message_subject_placeholder = models.CharField(max_length=100, blank=True)
    message_placeholder = models.CharField(max_length=100, blank=True)
    message_button = models.CharField(max_length=50, blank=True)

    contact_info_title = models.CharField(max_length=100, blank=True)
    contact_address_title = models.CharField(max_length=50, blank=True)
    contact_address = models.CharField(max_length=500, blank=True)
    contact_email_title = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(max_length=300, blank=True)
    contact_phone_title = models.CharField(max_length=50, blank=True)
    contact_phone = PhoneNumberField(blank=True)

    contact_facebook = models.URLField(max_length=500, blank=True)
    contact_twitter = models.URLField(max_length=500, blank=True)
    contact_instagram = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name = "content"

    def __str__(self):
        return self.content_name
