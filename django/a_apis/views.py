from django.shortcuts import render


def image_upload_view(request):
    return render(request, "image/list.html")
