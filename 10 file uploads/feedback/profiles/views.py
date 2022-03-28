from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'profiles/create_profile.html', {'form': form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            # video tutorial:
            profile = UserProfile(image=request.FILES['user_image'])

            # experiment:
            # profile = UserProfile(
            #     image=submitted_form.cleaned_data['user_image']
            # )
            profile.save()

            return HttpResponseRedirect('/profiles')

        return render(request, 'profiles/create_profile.html', {'form': submitted_form})
