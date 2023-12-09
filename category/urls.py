from django.urls import path

from .views import add_category, delete_category, edit_category, show_categories

urlpatterns = [
    path("add-category/", add_category, name="add_category"),
    path("show-category/", show_categories, name="show_categories"),
    path("edit-category/<int:category_id>/", edit_category, name="edit_category"),
    path("delete-category/<int:category_id>/", delete_category, name="delete_category"),
]
