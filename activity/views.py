from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# rest framework
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @csrf_exempt
# def index(request):
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def index(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
