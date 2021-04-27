from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

import sweetify


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            sweetify.sweetalert(request, 'Profile updated', timer=1000)
        else:
            sweetify.sweetalert(request, 'Update failed. Please ensure the form is vaild', timer=1000)
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
