from django.conf.urls import url, include
from frontend.views.landing import home
from frontend.views.assistant import document

document_urls = [
    url(r'^create/$', document.LossCreateForm.as_view(), name='create_document')
]

urlpatterns = [
    url(r'^$', home.HomeView.as_view(), name='home'),
    url(r'^document/', include(document_urls), name='document')
]


