from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp.views import Record_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', Record_View, name="record_upload"),
]