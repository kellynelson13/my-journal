from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def entries_index(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'entries/index.html', { 'entries': entries })

@login_required
def entries_detail(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    moods_entry_doesnt_have = Mood.objects.exclude(id__in = entry.moods.all().values_list('id'))
    return render(request, 'entries/detail.html', {'entry': entry, 'moods': moods_entry_doesnt_have})

@login_required
def assoc_mood(request, entry_id, mood_id):
  # Note that you can pass a mood's id instead of the whole object
  Entry.objects.get(id=entry_id).moods.add(mood_id)
  return redirect('detail', entry_id=entry_id)


@login_required
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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)





class EntryCreate(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ('date', 'entry')

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        return super().form_valid(form)

class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ('date', 'entry')

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = '/entries/'


class MoodList(LoginRequiredMixin, ListView):
    model = Mood
    template_name = 'moods/index.html'

class MoodDetail(LoginRequiredMixin, DetailView):
    model = Mood
    template_name = 'moods/detail.html'

class MoodCreate(LoginRequiredMixin, CreateView):
    model = Mood
    fields = '__all__'
    success_url = '/moods/'

class MoodUpdate(LoginRequiredMixin, UpdateView):
    model = Mood
    fields = '__all__'

class MoodDelete(LoginRequiredMixin, DeleteView):
    model = Mood
    success_url = '/moods/'

