from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)

        if entered_username == '':
            return render(request, 'reviews/review.html', {'has_error': True}) # {'has_error': True}: extra context pass to the template

        return HttpResponseRedirect('/thank-you')

    return render(request, 'reviews/review.html', {'has_error': False}) # {'has_error': False}: extra context pass to the template


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
