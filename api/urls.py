from django.urls import path
from api.views import *

app_name = "api"
urlpatterns = [
    path(route="index", view=Index.as_view(), name="index"),
    path(route="login", view=LoginView.as_view(), name="login"),
    path(route="deneme", view=RequestView.as_view(), name="deneme"),
]
