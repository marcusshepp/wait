from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from w.views import WorkoutViewSet
from users.views import LoginView, RegisterView

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Workout Tracker API",
        default_version='v1',
        description="API documentation for workout tracker",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@workouttracker.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
