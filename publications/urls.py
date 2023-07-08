
from django.urls import path

from . import views

app_name='publications'

urlpatterns = [
    path("",views.all_publications,name="all_publications"),
    #path("<int:blog_id>/",views.detail,name="detail"),

]
