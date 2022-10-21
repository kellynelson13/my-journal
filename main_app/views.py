from django.shortcuts import render
from django.http import HttpResponse


class Entry:
    def __init__(self, date, entry):
        self.date = date
        self.entry = entry

entries = [
    Entry('2022-04-05', 'This day is going really well so far'),
    Entry('2022-11-21', 'This is the day after my birthday')
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello MyJournal</h1>')


def about(request):
    return render(request, 'about.html')

def entries_index(request):
    return render(request, 'entries/index.html', { 'entries': entries })