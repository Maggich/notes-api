from django.urls import path

from .views import note_list, note_detail, task, product
from .serializers import NoteListView

urlpatterns = [
    path("notes/", note_list, name="note-list"),
    path("notes/<int:note_id>/", note_detail, name="note-detail"),
    path("task/", task, name="task-list"),
    path("product/", product, name="product-list"),
    path("api/notes/", NoteListView.as_view()),
]