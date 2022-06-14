from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *

@api_view(['GET'])
@csrf_exempt
def read(request, npm):
	try:
		mahasiswa = Mahasiswa.objects.get(npm=npm)
		return Response({
			'status': 'OK',
			'npm': mahasiswa.npm,
			'nama': mahasiswa.nama}, 
			status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		return Response({
			'status': 'ERROR',
			'message': 'Data not found'}, 
			status=status.HTTP_409_CONFLICT)

	