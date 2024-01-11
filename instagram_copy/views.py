from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("host with get")
        return render(request, "instagram_copy/main.html")

    def post(self, request):
        print("post with host")
        return render(request, "instagram_copy/main.html")