from types import SimpleNamespace

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import OperationalError
from django.views.decorators.cache import cache_page
from .models import Service, Project, TeamMember, Testimonial, MachineHire
from .forms import ContactForm, ConsultationForm


def build_service_fallback(title, description, static_image):
    return SimpleNamespace(
        title=title,
        description=description,
        image=None,
        image_url=f"{settings.STATIC_URL}{static_image}",
        icon='fa-tools',
    )


DEFAULT_SERVICES = [
    build_service_fallback(
        'General Construction Services',
        'We undertake full-scale construction projects for residential, commercial, and institutional clients. Our experienced team manages everything from site preparation and foundation to structural framing and external works, delivering durable, high-quality buildings on time and within budget.',
        'images/general-construction.jfif',
    ),
    build_service_fallback(
        'Design & Planning',
        'Our in-house architects and design engineers create functional, aesthetically refined plans tailored to your vision and budget. We handle concept development, detailed architectural drawings, structural designs, and obtain all necessary approvals from regulatory authorities.',
        'images/design-work.jpg',
    ),
    build_service_fallback(
        'Project Management',
        'Expert end-to-end project management ensures your construction project is delivered efficiently. We coordinate contractors, manage procurement, monitor quality, and provide regular progress reports — keeping your project on schedule and on budget at every stage.',
        'images/cart-excavator.jpg',
    ),
    build_service_fallback(
        'Renovation & Remodeling',
        'Breathe new life into your existing property with our renovation and remodeling services. From complete interior overhauls and room additions to kitchen upgrades, bathroom renovations, and façade improvements, we transform tired spaces into modern, functional environments.',
        'images/renovation-work.jfif',
    ),
    build_service_fallback(
        'Civil & Infrastructure Works',
        'We design and construct vital civil infrastructure including roads, bridges, drainage systems, water supply networks, and public utilities. Our civil engineering team brings technical expertise to every project, ensuring safe, durable, and code-compliant infrastructure.',
        'images/civil-and-infrastructure-works.webp',
    ),
    build_service_fallback(
        'Mechanical, Electrical & Plumbing (MEP)',
        'Complete mechanical, electrical, and plumbing installations handled by certified, experienced technicians. We provide dependable MEP solutions for buildings, ensuring performance, safety, and compliance across all systems.',
        'images/design-mechanical-electrical-works.jfif',
    ),
]


@cache_page(60 * 15, key_prefix='v2')
def home(request):
    featured_services = []
    featured_projects = []
    testimonials = []
    try:
        featured_services = list(Service.objects.filter(is_active=True)[:6])
        featured_projects = list(Project.objects.filter(is_featured=True)[:6])
        testimonials = list(Testimonial.objects.filter(is_active=True)[:6])
    except OperationalError:
        # Database is not yet migrated or available in production.
        featured_services = []
        featured_projects = []
        testimonials = []

    context = {
        'featured_services': featured_services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)


@cache_page(60 * 15, key_prefix='v2')
def services(request):
    all_services = []
    try:
        all_services = list(Service.objects.filter(is_active=True))
    except OperationalError:
        all_services = []

    if not all_services:
        all_services = DEFAULT_SERVICES.copy()
    else:
        existing_titles = {service.title.strip().lower() for service in all_services}
        for default_service in DEFAULT_SERVICES:
            if default_service.title.strip().lower() not in existing_titles:
                all_services.append(default_service)

    context = {'services': all_services}
    return render(request, 'services.html', context)


@cache_page(60 * 15, key_prefix='v2')
def projects(request):
    completed = []
    ongoing = []
    machines = []
    try:
        completed = list(Project.objects.filter(status='completed'))
        ongoing = list(Project.objects.filter(status='ongoing'))
        machines = list(MachineHire.objects.filter(is_available=True))
    except OperationalError:
        completed = []
        ongoing = []
        machines = []

    context = {
        'completed_projects': completed,
        'ongoing_projects': ongoing,
        'machines': machines,
    }
    return render(request, 'projects.html', context)


@cache_page(60 * 15, key_prefix='v2')
def about(request):
    team = []
    try:
        team = list(TeamMember.objects.filter(is_active=True))
    except OperationalError:
        team = []

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
                try:
                    contact_form.save()
                    messages.success(request, 'Thank you for reaching out! We will get back to you shortly.')
                    return redirect('contact')
                except OperationalError:
                    messages.error(request, 'The site is still starting up. Please try again in a moment.')
            else:
                messages.error(request, 'Please correct the errors below.')

        elif form_type == 'consultation':
            consultation_form = ConsultationForm(request.POST)
            if consultation_form.is_valid():
                try:
                    consultation_form.save()
                    messages.success(request, 'Your consultation has been booked! We will confirm shortly.')
                    return redirect('contact')
                except OperationalError:
                    messages.error(request, 'The site is still starting up. Please try again in a moment.')
            else:
                messages.error(request, 'Please correct the errors below.')

    context = {
        'contact_form': contact_form,
        'consultation_form': consultation_form,
    }
    return render(request, 'contact.html', context)