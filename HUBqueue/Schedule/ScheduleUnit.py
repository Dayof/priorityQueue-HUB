from django.shortcuts import render

class UiSchedule:

    def run(self,request):
        if request.method == "GET":
            return render(request, 'Queue/schedule.html', {})
            