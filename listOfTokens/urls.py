from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
  path('tokens/', views.index, name='index'),
  path('data/bsc/<int:num_tokens>/', views.bsc_tokens_view, name='tokens-view'),
  path('data/eth/<int:num_tokens>/', views.eth_tokens_view, name='tokens-view'),
  path('data/matic/<int:num_tokens>/', views.matic_tokens_view, name='tokens-view'),
  path('data/ftm/<int:num_tokens>/', views.ftm_tokens_view, name='tokens-view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
