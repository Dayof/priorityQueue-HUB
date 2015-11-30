from django.shortcuts import render

class UiRegister:

    def run(self,request):
        if request.method == "GET":
            return render(request, 'Register/reg_acc.html', {})
