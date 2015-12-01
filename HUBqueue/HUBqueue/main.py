from django.shortcuts import render
from django.http import HttpResponse
import json

class UiMain:

    def run(self,request):
        if request.method == "GET":
            return render(request, 'Register/home.html', {})
