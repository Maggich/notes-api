from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Note, Task, Product


def note_list(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    notes = list(Note.objects.values("id", "title", "text"))
    return JsonResponse({"items": notes})


def note_detail(request, note_id):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    
    note = get_object_or_404(Note, id=note_id)
    
    
    data = {
        "id": note.id,
        "title": note.title,
        "text": note.text
    }

    return JsonResponse(data)


def task(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    task = list(Task.objects.values("id", "task", "text_task"))

    return JsonResponse({"items": task})


def product(request):

    if request.method != "GET":
            return JsonResponse({"detail": "Method not allowed"}, status=405)

    product = list(Product.objects.values("id", "name", "description", "price"))

    return JsonResponse({"items": product})

