from django.shortcuts import render

def handler(request):
    return render(request, 'Register/reg_acc.html', {})