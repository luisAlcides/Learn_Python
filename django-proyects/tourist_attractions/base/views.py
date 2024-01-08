from django.shortcuts import render

# Create your views here.
attractions = [
  { 'attraction_name' : 'Niagra Falls', 'state' : 'New York'},
  { 'attraction_name' : 'Grand Canyon National Park', 'state' : 'Arizona'},
  { 'attraction_name' : 'Mall of America', 'state' : 'Minnesota'},
  { 'attraction_name' : 'Mount Rushmore', 'state' : 'South Dakota'},
  { 'attraction_name' : 'Times Square', 'state' : 'New York'},
  { 'attraction_name' : 'Walt Disney World', 'state' : 'Florida'}
]

def home(request):
    context = {'attractions': attractions}
    return render(request, 'base/home.html', context)

def details(request, statename):
    context = {'attractions': attractions}
    statename.replace("-", " ")
    return render(request, 'base/details.html', context)