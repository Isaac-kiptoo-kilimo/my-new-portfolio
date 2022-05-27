from django.urls import path
from . import views

urlpatterns=[
    path('',views.add_editor,name='Editor'),
    path('',views.add_project,name='project')
]