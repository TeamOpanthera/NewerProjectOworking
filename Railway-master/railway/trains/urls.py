from django.urls import path
from .views import AllTrainsListView,Bookings,TrainsDetailView,LogoutUserView,showHome
from .views import search,RegisterView, login_page,profile,BookingCancelDetailView, confirm_cancel,confirm_booking, ticket


urlpatterns = [
    # path('',HomeTemplateView.as_view(),name = 'home'),
    path('', showHome, name='home'),
    path('all/',AllTrainsListView.as_view(),name = 'all_trains'),
    path('all_booked/',Bookings.as_view(),name = 'all_booked'),
    path('trains/<int:pk>',TrainsDetailView.as_view(),name ='trains'),
    path('Ticket/',ticket,name='Ticket'),
    path('search/',search,name='search'),
    path('Register/',RegisterView.as_view(),name='Register'),
    path('login/',login_page,name='login'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('user/<slug:username>/',profile.as_view(),name='profile'),
    path('booking/<int:pk>/',BookingCancelDetailView.as_view(),name='cancel'),
    path('confirm_cancel/<int:pk>',confirm_cancel,name='confirm_cancel'),
    path('buy/<int:pk>',confirm_booking,name ='confirm_booking'),

]
