from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review


# Create your views here.
def index(request):
    if request.method == 'POST':
        # print(request.POST)
        form = ReviewForm(request.POST)
        # print(form)

        if form.is_valid():
            # print(form.cleaned_data['user_name'])
            '''
            # experiment:
            Review.objects.create(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating']
            )
            '''

            # video tutorial:
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating']
            )
            review.save()
            
            return HttpResponseRedirect('/thank-you')

    else:
        form = ReviewForm()
        # print(form)

    return render(request, 'reviews/review.html', {'form': form})


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
