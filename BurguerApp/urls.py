from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('catalog_BurguerApp.urls')),
    path('auth/', include('auth_BurguerApp.urls')),
    path('', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('profile/', views.user_profile, name='user_profile'),
]

handler404 = 'BurguerApp.views.custom_page_not_found'
handler500 = 'BurguerApp.views.custom_error'
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

