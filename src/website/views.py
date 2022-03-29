from django.shortcuts import render

from django.shortcuts import render,redirect
from website.forms import ContactUs
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings
from django.http import Http404
from .models import Project, Service, Partner, Team, Counter, Content


def index(request):

    try:
        content = Content.objects.filter(profile_name='e')
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    try:
        project = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Project does not exist")

    try:
        service = Service.objects.all()
    except Service.DoesNotExist:
        raise Http404("Service does not exist")

    try:
        partner = Partner.objects.all()
    except Partner.DoesNotExist:
        raise Http404("Partner does not exist")

    try:
        team = Team.objects.all()
    except Project.DoesNotExist:
        raise Http404("Team does not exist")

    try:
        counter = Counter.objects.all()
    except Counter.DoesNotExist:
        raise Http404("Counter does not exist")

    form = ContactUs(request.POST or None)
    if form.is_valid():
        subject = 'Subject:' + form.cleaned_data['subject']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        message = form.cleaned_data['message']
        recipient_list = [settings.EMAIL_HOST_USER]
        email_message = EmailMessage(subject, message, from_email, recipient_list, reply_to=[email])
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('Un en-tête non valide a été détecté.')

    context = {
        'content': content,
        'project': project,
        'service': service,
        'partner': partner,
        'team': team,
        'counter': counter
    }

    return render(request, "base.html", context)