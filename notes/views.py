from django.shortcuts import render
from .models import Notes

# Create your views here.

def index_view(request):

  notes = Notes.objects.all()

  context = {
    'notes': notes,
    'hobbies': ['Fishing', 'Badminton', 'Cycling']
  }

  return render(request, 'index.html', context)