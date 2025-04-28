from django.urls import path
from .views import pages_list, page_detail, PageCreateView, PageUpdateView, PageDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', pages_list, name='pages_list'),
    path('<int:pk>/', page_detail, name='page_detail'),
     path('crear/', PageCreateView.as_view(), name='page_create'),
     path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
     path('<int:pk>/eliminar/', PageDeleteView.as_view(), name='page_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)