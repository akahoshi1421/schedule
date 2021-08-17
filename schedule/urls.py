from django.urls import path
from . import views

urlpatterns = [
	path('', views.top, name='top'),
	path("<int:year>/<int:month>/<int:day>", views.tasks, name="tasks"),
	path("<int:year>/<int:month>/<int:day>/<int:id>", views.edit, name="edit"),
	path("create", views.create, name="create"),
	path("<int:year>/<int:month>/<int:day>/<int:id>/delete", views.delete, name = "delete"),
]