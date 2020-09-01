from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

#Por que el cambio de url_patterns a page_patterns
pages_patterns = ([
    
    # Las urls convencionales son tipo:
    # path('pages', include('core.urls'))

    #Se devuelve cuna class bassed view como vista.asview()
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    
    #Se devuelve como una vista
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),

], 'pages')