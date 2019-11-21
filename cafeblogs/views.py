from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
	"""The home page for cafeblogs."""
	return render(request, 'cafeblogs/index.html')

def topics(request):
 	"""Show all topics."""
 	topics = Topic.objects.order_by('date_added')
 	context = {'topics': topics}
 	return render(request, 'cafeblogs/topics.html', context)

def topic(request, topic_id):
	"""Show a single topic and all its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'cafeblogs/topic.html', context)