from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .forms import UserCreationForm, UserForm, ProfileForm
from .models import Profile


@login_required
def userpage(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    orders = request.user.order_set.all()
    context = {"user": request.user, "orders": orders,
               "user_form": user_form, "profile_form": profile_form}
    return render(request=request, template_name="registration/profile.html", context=context)



