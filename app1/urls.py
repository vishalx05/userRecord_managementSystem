from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('records/',views.records,name="records"),
   path('delete/<int:id>',views.delete,name="delete"),
   path('edit/<int:id>',views.edit,name="edit"),
   path('update/<int:id>',views.update ,name="update"),

]
