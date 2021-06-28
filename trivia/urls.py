from django.contrib import admin
from django.urls import path, include

""" '/<int:number>/' - чтобы поймать число из url и записать его в переменную number"""

urlpatterns = [
    path('topic/', include('topic.urls')),
    path('admin/', admin.site.urls),
]
