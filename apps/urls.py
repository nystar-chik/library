from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('book', BookModelViewSet)
# router.register('category', CategoryModelViewSet)
# router.register('info', InfoModelViewSet)
# router.register('teg', TegModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('books/', BookViewSets.as_view({'get': 'list', 'post' : 'create'})),
    # path('books/<int:pk>/', BookViewSets.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'})),
    # path('category/', CategoryViewSets.as_view({'get': 'list', 'post' : 'create'})),
    # path('category/<int:pk>/', CategoryViewSets.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'})),
    # path('info/', InfoViewSets.as_view({'get': 'list', 'post' : 'create'})),
    # path('info/<int:pk>/', InfoViewSets.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'})),
    # path('teg/', TegViewSets.as_view({'get': 'list', 'post' : 'create'})),
    # path('teg/<int:pk>/', TegViewSets.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'}))
]