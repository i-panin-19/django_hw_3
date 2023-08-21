from django.urls import path

from shop.views import IndexListView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, \
    toggle_activity

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('publication/<int:pk>/', toggle_activity, name='toggle_activity'),
]
