from django.shortcuts import render
from django.http import JsonResponse
import os
import json

def get_json_data(request):
    file_path = os.path.join(os.path.dirname(__file__), 'C:\python\project\project\myapp\locale\english.json')

    with open(file_path, 'r') as file:
        json_data = json.load(file)

    return JsonResponse(json_data)

