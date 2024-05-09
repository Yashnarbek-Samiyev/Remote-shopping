from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('add/favorites/<int:product_id>/',
         views.add_to_favorites, name='add_to_favorites'),
    path('remove/favorites/<int:product_id>/',
         views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites, name='favorites'),
    path('search/', views.search, name='search'),
    path('filter/<slug:slug>/', views.filter_by_category,
         name='filter_by_category'),
]
