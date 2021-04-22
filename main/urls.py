from django.urls import path
from .views import homePageView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView, dashboard,SignUpView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', homePageView.as_view(), name='home')
]
