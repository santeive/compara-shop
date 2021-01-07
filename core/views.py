from django.views.generic.base import TemplateView
from django.shortcuts import render
import sqlite3

class HomePageView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        with sqlite3.connect("stores.sqlite3") as conn:
            cursorObj = conn.cursor()
            
            #Products
            cursorObj.execute('SELECT count(id) FROM linio')
            products = cursorObj.fetchone()

            #Brands
            cursorObj.execute('SELECT count(DISTINCT brand) FROM linio')
            brands = cursorObj.fetchone()

            #Categories
            cursorObj.execute('SELECT COUNT(DISTINCT category) FROM linio')
            rows = cursorObj.fetchone()

            #Sellers
            cursorObj.execute('SELECT COUNT(DISTINCT seller) FROM linio')
            seller = cursorObj.fetchone()

            context = {
                'categories': rows[0],
                'products': products[0],
                'brands': brands[0],
                'seller': seller[0]
            }
            return render(request, "core/home.html", context)

class SamplePageView(TemplateView):
    template_name = "core/sample.html"