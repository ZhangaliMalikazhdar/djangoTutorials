from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='resuilts'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
