from django.shortcuts import render, redirect
from django.http import Http404

from users.models import User, Company, Customer
from services.models import Service, ServiceRequest
from datetime import datetime


def home(request):
    return render(request, 'users/home.html', {'user': request.user})


def customer_profile(request, name):
    # Fetch the customer user and service history
    try:
        user = User.objects.get(username=name)
        if not user.is_customer:
            if user.is_company:
                return redirect('company_profile', name=name)
            raise Http404("User is not a customer")
        
        # Fetch service requests for this customer
        service_requests = ServiceRequest.objects.filter(user=user).order_by('-requested_at')
        
        try:
            customer = Customer.objects.get(user=user)
            birth_date = customer.birth if customer.birth else None
        except Customer.DoesNotExist:
            birth_date = None
        
        return render(request, 'users/profile.html', {
            'user': user, 
            'service_requests': service_requests,
            'birth_date': birth_date
        })
    except User.DoesNotExist:
        raise Http404("User does not exist")


def company_profile(request, name):
    try:
        user = User.objects.get(username=name)
        if not user.is_company:
            if user.is_customer:
                return redirect('customer_profile', name=name)
            raise Http404("User is not a company")
            
        # Fetch company services
        try:
            company = Company.objects.get(user=user)
            services = Service.objects.filter(company=company).order_by("-date")
            return render(request, 'users/profile.html', {'user': user, 'services': services})
        except Company.DoesNotExist:
            raise Http404("Company profile does not exist")
    except User.DoesNotExist:
        raise Http404("User does not exist")
