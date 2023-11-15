from django.shortcuts import render
from .models import Files

def index(request):
    
    if request.method == "POST":
        files = request.FILES.getlist('files')
        for file in files:
            new_file = Files.objects.create(
                file = file
            )
            new_file.save()
            
    context = {'new_file':new_file}
    return render(request, 'base/index.html', context)
