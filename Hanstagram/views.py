from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("Get")
        return render(request, "Hannstagram/main.html")

    def post(self, request):
        print("Post")
        return render(request, "Hanstagram/main.html")