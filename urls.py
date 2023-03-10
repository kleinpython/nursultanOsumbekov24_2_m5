from django.contrib import admin
from django.urls import path
from Afisha import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_list_api_view),
    path('api/v1/directors/<int:id>/', views.director_id_list_api_view),
    path('api/v1/movies/reviews/', views.movie_list_api_view),
    path('api/v1/movies/<int:id>/', views.movie_id_list_api_view),
    path('api/v1/reviews/', views.review_list_api_view),
    path('api/v1/reviews/<int:id>/', views.review_id_list_api_view),]