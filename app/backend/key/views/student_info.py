from django.core import serializers
from ..models import StudentInfo
from ..serializers import StudentInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time


class StudentInfo(APIView):

    def validateGet(self, request):
        if 'id' in request.query_params:
            try:
                StudentInfo.objects.get(pk=int(request.query_params['id']))
            except Exception as e:
                return False

        return True
      
    def validatePatch(self, request):
        try:
            StudentInfo.objects.get(pk=request.data['id'])
        except:
            return False
        return True

    # Get existing student data
    def get(self, request):
        if not self.validateGet(request):
            return Response({'error':'Invalid Parameters'}, status='400')

        info = StudentInfo.objects.all()
        if 'student_id' in request.query_params:
            student = StudentsInfo.objects.filter(pk=request.query_params['student_id'])
            serializer = StudentInfoSerializer(student)
        else:
            students = StudentsInfo.objects.all()
            serializer = StudentInfoSerializer(students, many=True)
        
        return Response(serializer.data, content_type='application/json')
      
    # Create a new student
    def post(self, request):
        # Note: Until we convert student.id to an autofield/serial, this will require that we create a new student ID for new students.
        # So, for now we'll just assign them the UNIX timestamp, since that should be pretty unique.
        # This approach will break on January 17, 2038, when UNIX timestamps will exceed 32 bits, so we'll probably want to fix this.
        if not 'id' in request.data:
            request.data['id'] = round(time.time())

        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing student
    def patch(self, request):
        if not self.validatePatch(request):
            return Response({'error':'Invalid Paremeters'}, status='400')

        obj = StudentInfo.objects.get(pk=request.data['id'])
        serializer = StudentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
