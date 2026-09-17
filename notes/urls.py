from django.urls import path

from .views import task, product, NoteListView


urlpatterns = [
    path("task/", task, name="task-list"),
    path("product/", product, name="product-list"),
    path("notes/", NoteListView.as_view()),
]