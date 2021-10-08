from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import province_choices, bedrooms_choices, price_range


def index(request):
    # Get all published listings ordered by list date
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'province_choices': province_choices,
        'bedrooms_choices': bedrooms_choices,
        'price_range': price_range,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
