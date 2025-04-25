from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django.views import View

class ApiTestView(View):
    def get(self, request):
        return JsonResponse({"status": "ok", "mensaje": "GET recibido correctamente"})

    def post(self, request):
        return JsonResponse({"status": "ok", "mensaje": "POST recibido correctamente"})


class TestViews(APIView):

    def get(self, request, *args, **kwargs):
        return Response("Holaa Mundo")