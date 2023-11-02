from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed  # models 에서 Feed 클래스 호출

# Create your views here.
# 이전의 Views와 다른 점 => model을 통해 Db를 불러와서 보여주겠다!
class Main(APIView):
    def get(self, request):
        print("get으로 호출")

        # Feed 클래스의 모든 object를 가져오겠어!!
        feed_list = Feed.objects.all() # 이게 console에 작성한 select * from fake_insta_feed;와 같음

        # print(feed_list) # 어떻게 db가 불러와지는지 확인용
        # for feed in feed_list: print(feed.content) # 확인용

        return render(request, "fake_instagram/main.html", context=dict(feeds=feed_list))