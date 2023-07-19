from django.shortcuts import render
from .models import Topic
from django.http import FileResponse
import os
from .models import SubjectEntry
#from .models import Entry
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.conf import settings
from django.http import HttpResponse
from django.http import Http404


# Create your views here.
def index(request):
    return render(request,'compsite_pro/index.html')

def about(request):
    return render(request,'compsite_pro/about.html')


def coming(request):
    return render(request,'compsite_pro/coming.html')

def base(request):
    return render(request,'compsite_pro/base.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'compsite_pro/topics.html',context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entries.all()
    context = {'topic': topic,'entries':entries}
    return render(request, 'compsite_pro/topic.html', context)

def notice(request, topic_id):
    notices = notice.entries.all()
    context = {'entry': notice,'notices':notices}
    return render(request, 'compsite_pro/topic.html', context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404



