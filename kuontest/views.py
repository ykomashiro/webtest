# Create your views here.
import json

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View


def index(request):
    return HttpResponse("Hello, guest, You're at the network test index page.")


class ImageDealView(View):
    '''ImageDeal'''
    def get(self, request):
        received_json_data = json.loads(request.body)
        print(received_json_data)
        return HttpResponse(json.dumps({'detail': "GET Response"}))

    def post(self, request):
        received_json_data = json.loads(request.body)
        try:
            print(received_json_data['pictureId'])
            print(received_json_data['code'])
            print(received_json_data['attach'])
        except:
            print(received_json_data)
        return HttpResponse(json.dumps({'detail': "POST Response"}))
