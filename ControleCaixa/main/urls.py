from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('',views.main,name="main"),
    path('caixas',views.caixas,name="caixas"),
    path('clientes',views.clientes,name="clientes"),
    path('emprestimo/<caixa_cod>/<cliente_cod>',views.emprestimo,name="emprestimo"),
    path('deleteCaixa/<caixa_id>',views.deleteCaixa,name="delete-Caixa"),
    path('deleteCliente/<cliente_id>',views.deleteCliente,name="deleteCliente"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)