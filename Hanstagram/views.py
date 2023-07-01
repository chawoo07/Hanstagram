from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("GET")
        return render(request, "hanstagram/main.html")

    def post(self, requst):
        print("POST")
        return render(requst, "hanstagram/main.html")