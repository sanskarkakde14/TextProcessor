from django.contrib import admin
from django.urls import path
from djangoProject import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
]