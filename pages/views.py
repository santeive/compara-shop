# from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

#Esisten dos vistas basadas en clases
# Para cuando tengamos que devolver las instancias de un modelo (ListView)
# Para cuando tengamos que devolver una instancia de un modelo (DetailView)

# Esta clase se hereda a las otras clases que queramos combinar la autenticación
# Object es la clase base de todas las clases en python
class StaffRequiredMixin(object):
    ''' Este mixin requerirá que el susuario sea parte del staff '''
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')