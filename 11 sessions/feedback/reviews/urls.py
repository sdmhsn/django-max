from django.urls import path

from . import views


urlpatterns = [
    path('', views.ReviewView.as_view()), # urlpattern required for class based view
    path('thank-you', views.ThankYouView.as_view()),
    path('review-list', views.ReviewListView.as_view()),
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    path('review/<int:pk>', views.SingleReviewView.as_view()),
]
