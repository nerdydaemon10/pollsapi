from django.urls import path

from polls.views import PollsDetailApiView, PollsListApiView


urlpatterns = [
    # GET /api/polls/
    path('', PollsListApiView.as_view()),
    path('<int:pk>/', PollsDetailApiView.as_view()),
    path('<int:pk>/was-created-recently/', PollsDetailApiView.was_created_recently())
]