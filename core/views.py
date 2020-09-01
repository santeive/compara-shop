from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        return render(request, "core/home.html", {'title':"Larva Platform"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"