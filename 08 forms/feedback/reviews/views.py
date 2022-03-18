from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        # print(request.POST)
        form = ReviewForm(request.POST)
        # print(form)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')

    form = ReviewForm()
    # print(form)

    return render(request, 'reviews/review.html', {'form': form})


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
