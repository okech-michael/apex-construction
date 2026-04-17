from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Project, TeamMember, Testimonial, MachineHire
from .forms import ContactForm, ConsultationForm


def home(request):
    featured_services = Service.objects.filter(is_active=True)[:6]
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    context = {
        'featured_services': featured_services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)


def services(request):
    all_services = Service.objects.filter(is_active=True)
    context = {'services': all_services}
    return render(request, 'services.html', context)


def projects(request):
    completed = Project.objects.filter(status='completed')
    ongoing = Project.objects.filter(status='ongoing')
    machines = MachineHire.objects.filter(is_available=True)
    context = {
        'completed_projects': completed,
        'ongoing_projects': ongoing,
        'machines': machines,
    }
    return render(request, 'projects.html', context)


def about(request):
    team = TeamMember.objects.filter(is_active=True)
    context = {'team': team}
    return render(request, 'about.html', context)


def contact(request):
    contact_form = ContactForm()
    consultation_form = ConsultationForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'contact':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Thank you for reaching out! We will get back to you shortly.')
                return redirect('contact')
            else:
                messages.error(request, 'Please correct the errors below.')

        elif form_type == 'consultation':
            consultation_form = ConsultationForm(request.POST)
            if consultation_form.is_valid():
                consultation_form.save()
                messages.success(request, 'Your consultation has been booked! We will confirm shortly.')
                return redirect('contact')
            else:
                messages.error(request, 'Please correct the errors below.')

    context = {
        'contact_form': contact_form,
        'consultation_form': consultation_form,
    }
    return render(request, 'contact.html', context)