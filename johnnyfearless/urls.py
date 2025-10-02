# urls.py


from django.contrib import admin
from django.urls import path
from johnnyfearless.views import *  #replace django_demo with your own app name
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home_page_path"),
    path('contact/', contact_page, name="contact_page_path"),
    path('form/', form_page, name="form_page_path"),
    path('user_list/', user_list, name="user_list_path"),
    path('Update/<int:user_id>/', user_update, name="user_update_path"),
    path('Delete/<int:user_id>/', user_delete, name="user_delete_path"),
    path('product/', product_list, name="product_path"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 