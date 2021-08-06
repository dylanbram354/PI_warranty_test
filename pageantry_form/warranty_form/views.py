from django.shortcuts import render
from .models import Warranty
from .serializers import WarrantySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class WarrantyList(APIView):

    def post(self, request):
        serializer = WarrantySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        entries = Warranty.objects.all()
        serializer = WarrantySerializer(entries, many=True)
        return Response(serializer.data)

