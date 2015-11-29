from django.shortcuts import render

def handler(request):
    return render(request, 'Queue/schedule.html', {})