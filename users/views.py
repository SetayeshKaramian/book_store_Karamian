from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserCreationForm, UserForm, ProfileForm


@login_required
def userpage(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    orders = request.user.order_set.all()
    print("ORDERS:", orders)
    # context={'orders': }
    return render(request=request, template_name="registration/profile.html",
                  context={"user": request.user, "user_form": user_form, "profile_form": profile_form})
