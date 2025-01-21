from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [path('products/',views.products,name='products'),
               path('add/',views.add,name='add'),
               path('',views.register,name='register'),
               path('login/',auth_views.LoginView.as_view(),name='login'),
               path('logout/',auth_views.LogoutView.as_view(),name='logout'),
               path('delete/<int:id>/',views.delete,name='delete'),
               path('update/<int:id>',views.update,name='update'),
               ]
if settings.DEBUG :
   urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)