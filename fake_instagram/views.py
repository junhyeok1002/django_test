from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "fake_instagram/main.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "fake_instagram/main.html")

class Sub1(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "fake_instagram/1.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "fake_instagram/1.html")

class Sub2(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "fake_instagram/2.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "fake_instagram/2.html")

class Sub3(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "fake_instagram/3.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "fake_instagram/3.html")