from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:question_id>/', DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='resuilts'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
