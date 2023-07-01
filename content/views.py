import os.path
from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
import os
from user.models import User
from Hanstagram.settings import MEDIA_ROOT


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # Order_by('-id') : 最新順に
        # select * from content_feed;

        # ログイン情報
        print('ログインしているユーザー：', request.session['email'])

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, "Hanstagram/main.html", context=dict(feeds=feed_list, user=user))


# Create your views here.

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

            file = request.data.get('file')

        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)
        # status 200は成功
        return Response(status=200)


class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")
        return render(request, 'content/profile.html', context=dict(user=user))


