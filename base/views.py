from django.shortcuts import render
from .models import Files

def index(request):
    if request.method == "POST":
        files = request.FILES.getlist('files')
        file_list = []
        for file in files:
            new_file = Files(
                file = file
            )
            new_file.save()
            file_list.append(new_file.file.url)
    else:
        return render(request, 'base/index.html')
    context = {'new_urls':file_list}
    return render(request, 'base/index.html', context)
