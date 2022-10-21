from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Entry, Mood, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'myjournal-nova'



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
    moods_entry_doesnt_have = Mood.objects.exclude(id__in = entry.moods.all().values_list('id'))
    return render(request, 'entries/detail.html', {'entry': entry, 'moods': moods_entry_doesnt_have})

def assoc_mood(request, entry_id, mood_id):
  # Note that you can pass a mood's id instead of the whole object
  Entry.objects.get(id=entry_id).moods.add(mood_id)
  return redirect('detail', entry_id=entry_id)


def add_photo(request, entry_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to entry_id or entry (if you have a entry object)
            photo = Photo(url=url, entry_id=entry_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', entry_id=entry_id)





class EntryCreate(CreateView):
    model = Entry
    fields = ('date', 'entry')

class EntryUpdate(UpdateView):
    model = Entry
    fields = ('date', 'entry')

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

class MoodUpdate(UpdateView):
    model = Mood
    fields = '__all__'

class MoodDelete(DeleteView):
    model = Mood
    success_url = '/moods/'

