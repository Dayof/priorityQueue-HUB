#coding: utf-8

from django.shortcuts import render

class UiRegister:

    def run(self,request, model=None):
        if request.method == "GET":

            if model:
                if model=="patient":
                     url = "Register/reg_pat.html"
                elif model=="medic":
                     url = "Register/reg_med.html"
                elif model=="regulador":
                     url = "Register/reg_reg.html"
                # Tratar error de model que não existe no sistema.
            else:
                url = "Register/reg_acc.html"

            return render(request, url , {})
