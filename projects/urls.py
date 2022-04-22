from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_project, name='create_project'),
    path("get/", views.get_projects, name="view_all_projects"),
    path("filter/", views.filter_projects),
    path("get/<int:id>", views.retrieve_project, name='project_detail'),
    path("update/<int:id>", views.update_project, name='update_project'),
    path("delete/<int:id>", views.delete_project, name='delete_project')
]