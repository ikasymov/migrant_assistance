from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from authentication import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'signin/$', views.SignInView.as_view(), name='sign_in'),
    url(r'signup/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^', include('frontend.urls'), name='frontend')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
