from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .api import ListViewSet, CardViewSet

from . import views

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)
# router.register(r'cardInfo', views.cardInfo)
urlpatterns = [
        url(r'^cardInfo/(?P<id>\w+)/$', views.card_info_view),
        url(r'^', include(router.urls)),
    ]
# urlpatterns = [
#     url(r'^lists$', ListApi.as_view()),
#     url(r'^cards$', CardApi.as_view()),
#     url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html"))
# ]