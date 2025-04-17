from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.db.models import Count
from services.models import ServiceRequest, Service

def home(request):
    return render(request, "main/home.html", {})

def logout(request):
    django_logout(request)
    # Redirect to homepage
    return redirect('/')

def top_services(request):
    """
    View to display the top 10 most requested services
    """
    # Query the database to count service requests by service
    top_services_data = ServiceRequest.objects.values(
        'service'
    ).annotate(
        request_count=Count('id')
    ).order_by('-request_count')[:10]
    
    # Get the informations for each service
    top_services = []
    for item in top_services_data:
        service = Service.objects.get(id=item['service'])
        top_services.append({
            'service_id': service.id,
            'name': service.name,
            'field': service.field,
            'company_username': service.company.user.username,
            'request_count': item['request_count']
        })
    
    context = {
        'top_services': top_services
    }
    
    return render(request, 'main/top_services.html', context)
