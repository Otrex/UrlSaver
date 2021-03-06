from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Upload

# Create your views here.

def index(request):
	files = Upload.objects.all()
	print(files)
	return render(request, 'uploader/index.html', {"files" : files, 'cnt': 0})

def upload_file(f):
	print(dir(f))


def get(request):
	if request.method == 'POST':
		print(request.FILES["fileD"])
		Upload(caption="obi", file = request.FILES["fileD"]).save()
	else : return HttpResponse(" Failed to upload ")
	return redirect("/uploader/")


@require_http_methods(["GET"])
def delete(request, tid):
    tid = Upload.objects.get(id = tid)
    info = tid.caption
    tid.delete()
    return HttpResponse("URL '{}' has been DELETED SUCCESSFULLY....<script> setTimeout(()=>window.location.href='http://localhost:8000/uploader/', 5000) </script>".format(info))