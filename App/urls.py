from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path ('login', views.login, name='login'),
    path ('signup', views.signup, name='signup'),
    path ('logout', views.logout, name='logout'),
    path ('about', views.about, name='about'),
    path ('service', views.service, name='service'),
    path ('home/birds', views.home, name='home'),
    path ('market', views.market, name='market'),
    path ('birds/varieties/<str:id>', views.varieties, name='varieties'),
    path ('birds/<str:id>', views.read, name='read'),
    path ('home/crops', views.crop, name='crop'),
    path ('crops/varieties/<str:id>', views.crops, name='cropvarieties'),
    path ('crops/<str:id>', views.readcrops, name='readcrops'),
    path ('market/productvarieties/<str:id>', views.products, name='productvarieties'),
    path ('market/<str:id>', views.readproduct, name='readproduct'),
    path ('cart', views.cart, name='cart'),
    path ('checkout', views.checkout, name='checkout'),
    path ('payment', views.payment, name='payment'),
    # path ('update_item', views.updateItems, name='updateItem'),
]


urlpatterns += staticfiles_urlpatterns()