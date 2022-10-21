from django.shortcuts import render
from .models import Entry



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
