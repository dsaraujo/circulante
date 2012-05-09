from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('catalogar', 'catalogo.views.catalogar'),
    ('editar/(\d+)', 'catalogo.views.editar'),
    ('', 'catalogo.views.busca'),
    ('^$', 'django.views.generic.simple.direct_to_template',    
     {'template': 'home.html'}),     
)
