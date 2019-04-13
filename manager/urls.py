# # We use the function `path` to tell Django how we want our URLs to look like
# from django.urls import path
#
# # The views are here because we map each URL to a view we have created
# from manager import views
#
#
# # Django will look for a variable called `urlpatterns` and load the URLs
# # defined in it
# urlpatterns = [
#     path('task/', views.list_tasks),
#     path('board/<int:pk>/', views.get_board)
# ]

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from manager.views import TaskViewSet, BoardViewSet

# We define a router object. It will look at our viewsets, decide
# what URLs we need and create them automatically so we don't have to
router = DefaultRouter()
# Register the viewsets that the router must analyze
router.register(r'task', TaskViewSet, base_name='task')
router.register(r'board', BoardViewSet, base_name='board')


# The variable `urlpatterns` will simply receive the URLs computed by the router
# Lets open a shell, import the variable `router` and have a look at the URLs
# it produces
urlpatterns = router.urls