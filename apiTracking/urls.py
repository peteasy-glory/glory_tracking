# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from banjjak_tracking import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='html/api_traking/index.html')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
