# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic

class handler404(generic.View):
    def get(self, request):
        return render(request, "404.html", "")