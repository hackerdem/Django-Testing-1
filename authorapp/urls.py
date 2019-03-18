from django.urls import path
from .views import AuthorCreateView, CreateSuccessView

urlpatterns = [ 
    path('create', AuthorCreateView.as_view(),name='author-create'),
    path('success', CreateSuccessView.as_view(),name='success')

]
