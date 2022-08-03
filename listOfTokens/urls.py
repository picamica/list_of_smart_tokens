from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
  path('tokens/', views.index, name='index'),
  path('data/bsc/', views.bsc_tokens_view, name='tokens-view'),
  path('data/eth/', views.eth_tokens_view, name='tokens-view'),
  path('data/matic/', views.matic_tokens_view, name='tokens-view'),
  path('data/ftm/', views.ftm_tokens_view, name='tokens-view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
