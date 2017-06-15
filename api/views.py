import numpy as np
np.random.seed(1337)

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Photos
from .serializers import PhotoSerializer
from rest_framework import status
from django.core.files.base import ContentFile
import os
from PIL import Image


# process image after upload
def process_image(image_name, file_content):
    folder = './temp/'
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # create the folder if it doesn't exist.
    try: os.mkdir(os.path.join(BASE_PATH, folder))
    except: pass
    # save the uploaded file inside that folder.
    try:
        img_fullpath = os.path.join(BASE_PATH, folder, image_name)
        fout = open(img_fullpath, 'wb+')
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
    except Exception as exp: raise exp
    img = np.array(Image.open(img_fullpath).convert('RGB'))
    return img, img_fullpath


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PhotoList(APIView):
    """
    This end point is to recive from-data of two images and an imgid

    field: imgid, type: string
    field: file1, type: file
    field: file2, type: file
    """
    def get(self, request, format=None):
        return Response({'mgs': 'not applied api end point'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        imgid = request.POST['imgid']
        print('recieved image id:', imgid)

        try:
            image_one = request.FILES['file1'].name
            file_content = ContentFile(request.FILES['file1'].read())
            image_one, img_one_fullpath = process_image(image_one, file_content)

            image_two = request.FILES['file2'].name
            file_content = ContentFile(request.FILES['file2'].read())
            image_two, img_two_fullpath = process_image(image_two, file_content)
        except Exception as exp:
            # raise exp
            return Response({'mgs': 'image processing failed'}, status=status.HTTP_204_NO_CONTENT)

        # do ypur prediction here
        # after prediction remove the file
        # return success message with predicted data : os.remove(img_path)

        print(type(image_one))
        print(img_one_fullpath)

        return Response({
            'mgs': 'success!!! checkout the full response :)',
            'key1': 'result1... so on'
            }, status=status.HTTP_200_OK)


class PhotoDetail(APIView):
    def get(self, request, pk, format=None):
        return Response({'mgs': 'not applied api end point'}, status=status.HTTP_501_NOT_IMPLEMENTED)
    
    def post(self, request, pk, format=None):
        return Response({'mgs': 'not applied api end point'}, status=status.HTTP_501_NOT_IMPLEMENTED)
