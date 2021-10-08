from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_title = request.POST['title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        realtor_name = request.POST['realtor_name']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'This listing has already an inquiry from this user.')
                return redirect(f'/listings/{listing_id}')

        user_contact = Contact(listing=listing_title, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        user_contact.save()

        """
        Send_email is an django app for sending email messages
        Parameters: subject, message, from_email, recipient_list, settings
        """
        '''
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for {}. Sign into the admin panel for more info'.format(listing_title),
            'system_email',
            [realtor_email],
            fail_silently=False
        )
        '''

        messages.success(request, f'Your request has been submitted and {realtor_name} will get back to you soon.')

        return redirect(f'/listings/{listing_id}')
