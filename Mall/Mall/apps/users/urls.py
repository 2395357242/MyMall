from django.urls import path, include
from django.views.generic.base import TemplateView
urlpatterns = [
    # path('admin/', admin.site.urls),
    # users
    path('register/', TemplateView.as_view(template_name="index.html"))

]
