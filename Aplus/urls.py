from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('hello/', views.say_hello),
    path('', views.login_view, name='index'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),

    path('<int:user_grading>/grading/', views.grading, name='grading'),
    path('<int:gradeid>/excelupdate/', views.excelupdate, name='excelupdate'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

