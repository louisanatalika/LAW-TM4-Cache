from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def update(request):
	nama = request.data.get('Nama')
	npm = request.data.get('NPM')
	mahasiswa = Mahasiswa.objects.filter(npm = npm)

	if mahasiswa.exists():
		mahasiswa.update(nama = nama)
	else:
		Mahasiswa.objects.create(nama = nama, npm = npm)
	

	return Response({'status': 'OK'}, status=status.HTTP_200_OK)
