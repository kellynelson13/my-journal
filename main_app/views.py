from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Entry, Mood



# class Entry:
#     def __init__(self, date, entry):
#         self.date = date
#         self.entry = entry

# entries = [
#     Entry('2022-04-05', 'This day is going really well so far'),
#     Entry('2022-11-21', 'This is the day after my birthday')
# ]


# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def entries_index(request):
    entries = Entry.objects.all()
    return render(request, 'entries/index.html', { 'entries': entries })

def entries_detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render(request, 'entries/detail.html', {'entry': entry})


class EntryCreate(CreateView):
    model = Entry
    fields = '__all__'

class EntryUpdate(UpdateView):
    model = Entry
    fields = '__all__'

class EntryDelete(DeleteView):
    model = Entry
    success_url = '/entries/'


class MoodList(ListView):
    model = Mood
    template_name = 'moods/index.html'

class MoodDetail(DetailView):
    model = Mood
    template_name = 'moods/detail.html'

class MoodCreate(CreateView):
    model = Mood
    fields = '__all__'
    success_url = '/moods/'

