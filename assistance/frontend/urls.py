from django.conf.urls import url
from frontend.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
