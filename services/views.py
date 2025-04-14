from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from .models import Service, ServiceRequest
from .forms import RequestServiceForm

from users.models import Company

from .models import Service
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    # Only companies can create services
    if not request.user.is_company:
        return redirect('services_list')
    
    company = Company.objects.get(user=request.user)
    
    # Determine available field choices based on company's field
    if company.field == 'All in One':
        choices = Service.choices
    else:
        choices = [(company.field, company.field)]
    
    if request.method == 'POST':
        form = CreateNewService(request.POST, choices=choices)
        if form.is_valid():
            # Create a new service with the form data
            service = Service.objects.create(
                company=company,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price_hour=form.cleaned_data['price_hour'],
                field=form.cleaned_data['field']
            )
            # Redirect to the new service's detail page
            return redirect('index', id=service.id)
    else:
        form = CreateNewService(choices=choices)
    
    return render(request, 'services/create.html', {'form': form})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_request = ServiceRequest.objects.create(
                user=request.user,
                service=service,
                address=form.cleaned_data['address'],
                hours=form.cleaned_data['hours']
            )
            messages.success(request, f"Service '{service.name}' requested successfully!")
            return redirect('/')
    else:
        form = RequestServiceForm()
    return render(request, 'services/request_service.html', {'form': form, 'service': service})