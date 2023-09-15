from django.urls import path
from .views import CategoryCreateListView,CategoryRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('cats/',CategoryCreateListView.as_view(),name="cats"),
    path('cat/<int:pk>/',CategoryRetrieveUpdateDestroyAPIView.as_view(),name='cat_detail')
]
