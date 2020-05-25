from .views import CarViewSet
from rest_framework.routers import DefaultRouter

app_name = 'core'

router = DefaultRouter()
router.register(r'cars', CarViewSet, base_name='car')
urlpatterns = router.urls
