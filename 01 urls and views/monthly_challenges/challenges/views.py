from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 30 minutes every day',
    'march': 'Learn Django at least 20 minutes every day',
    'april': 'Eat no meat for the entire month',
    'may': 'Walk for at least 30 minutes every day',
    'june': 'Learn Django at least 20 minutes every day',
    'july': 'Eat no meat for the entire month',
    'august': 'Walk for at least 30 minutes every day',
    'september': 'Learn Django at least 20 minutes every day',
    'october': 'Eat no meat for the entire month',
    'november': 'Walk for at least 30 minutes every day',
    'december': 'Learn Django at least 20 minutes every day',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month number!')

    redirect_month = months[month - 1]
    # print(redirect_month)
    month_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(month_path)


def monthly_challenge(request, month):
    # challenge_text = None

    # if month == 'january':
    #     challenge_text = 'Eat no meat for the entire month'
    # elif month == 'february':
    #     challenge_text = 'Walk for at least 30 minutes every day'
    # elif month == 'march':
    #     challenge_text = 'Learn Django at least 20 minutes every day'
    # else:
    #     return HttpResponseNotFound('This month is not supported!')

    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        print(month_path)
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'

    return HttpResponse(response_data)


