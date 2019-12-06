from django.urls import path 
from . import views
urlpatterns = [
   path('sightings/',views.all_squirrels),
   path('map/',views.map),
   path('sightings/add/', views.add_squirrel),
   path('sightings/stats/',views.stats),
   path('sightings/<str:squirrel_id>/',views.edit_squirrel),
]

