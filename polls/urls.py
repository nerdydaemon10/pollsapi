from django.urls import path
from .views import PollsDetailApiView, PollsListApiView

urlpatterns = [
    path("", PollsListApiView.as_view()),
    path("<int:pk>/", PollsDetailApiView.as_view())
]