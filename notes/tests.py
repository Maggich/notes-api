import pytest
from django.urls import reverse

from .models import Note, Task


@pytest.mark.django_db
def test_note_is_saved():
    note = Note.objects.create(title="First note", text="Hello")

    assert note.title == "First note"
    assert Note.objects.count() == 1


@pytest.mark.django_db
def test_note_list_returns_notes(client):
    Note.objects.create(title="First note", text="Hello")

    response = client.get(reverse("note-list"))

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 1, "title": "First note", "text": "Hello"},
        ]
    }


def test_note_list_rejects_post(client):
    response = client.post(reverse("note-list"))

    assert response.status_code == 405


@pytest.mark.django_db
def test_note_detail_returns_note(client):
    
    note = Note.objects.create(title="First note", text="Hello")

  
    url = reverse("note-detail", kwargs={"note_id": note.id})
    response = client.get(url)

    
    assert response.status_code == 200
    
    
    assert response.json() == {
        "id": note.id,
        "title": "First note",
        "text": "Hello"
    }


@pytest.mark.django_db
def test_task_list_returns_tasks(client):
    Task.objects.create(task="First task", text_task="Hello")

    response = client.get(reverse("task-list"))

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 1, "task": "First task", "text_task": "Hello"},
        ]
    }