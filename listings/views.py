from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import province_choices, price_range, bedrooms_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_listing = Listing.objects.order_by('-list_date')

    # Search by Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listing = queryset_listing.filter(description__icontains=keywords)

    # Search by city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_listing = queryset_listing.filter(city__iexact=city)

    # Search by city
    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset_listing = queryset_listing.filter(province__iexact=province)

    # Search by city
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_listing = queryset_listing.filter(bedrooms__gte=bedrooms)

    # Search by city
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_listing = queryset_listing.filter(price__lte=price)

    paginator = Paginator(queryset_listing, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'province_choices': province_choices,
        'bedrooms_choices': bedrooms_choices,
        'price_range': price_range,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
