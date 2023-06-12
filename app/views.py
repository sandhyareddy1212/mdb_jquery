from django.shortcuts import render

# Create your views here.
def mdb_jquery(request):
    return render(request,'mdb_jquery.html')


def background_image(request):
    return render(request,'background_image.html')