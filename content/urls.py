from django.urls import path, re_path
from content.views import *

urlpatterns = [
    path('', content_index, name="index"),
    re_path(r'^content/(?P<id>\d+)/$', content_detail, name="detail")
]