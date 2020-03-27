from rest_framework.routers import DefaultRouter

from .api import ListViewSet, CardViewSet

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     url(r'^lists$', ListApi.as_view()),
#     url(r'^cards$', CardApi.as_view()),
#     url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html"))
# ]