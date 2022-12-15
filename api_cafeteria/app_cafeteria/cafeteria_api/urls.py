from django.urls import path
from .views import CafeteriaApiView, CafeteriaDetailApiView, CafeteriaClasificacionApiView
urlpatterns = [
    path('', CafeteriaApiView.as_view(), name="Cafeteria_List"),
    path('<int:cafeteria_id>/', CafeteriaDetailApiView.as_view(), name="Cafeteria_detail"),
    path('<slug:cafeteria_clasificacion>/', CafeteriaClasificacionApiView.as_view()),

]
