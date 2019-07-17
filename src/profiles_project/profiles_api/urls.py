from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")
router.register("profile", views.UserProfileViewSet)  # base_name not necessary for ModelViewSet
router.register("login", views.LoginViewSet, base_name="login")

urlpatterns = [
    url(r"^hello-view/", views.HelloApiView.as_view()),
    url(r"", include(router.urls)),
]
