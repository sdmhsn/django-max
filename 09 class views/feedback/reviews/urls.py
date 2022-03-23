from django.urls import path

from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.ReviewView.as_view()), # urlpattern required for class based view
    # path('thank-you', views.thank_you),
    path('thank-you', views.Thank_YouView.as_view()),
]
