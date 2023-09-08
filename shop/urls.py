from django.urls import path

from shop.views import IndexListView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, \
    toggle_activity, ProductCreateView, ProductUpdateView, VersionListView, VersionCreateView, VersionUpdateView, \
    VersionDeleteView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('publication/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('version/', VersionListView.as_view(), name='list_version'),
    path('version_create/', VersionCreateView.as_view(), name='create_version'),
    path('version_update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('version_delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),
]
