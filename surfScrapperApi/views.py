from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SubscriberFormSerializer


class SubmitSubscriberFormView(APIView):
    def post(self, request, format=None):
        print('Test_1')
        serializer = SubscriberFormSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print('Test_2')
            return Response({'message': 'Form submitted successfully!'}, status=status.HTTP_201_CREATED, content_type='application/json')
        else:
            print('cos tam jest zjebane')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)