from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recommendation.urls')),
    path('book_recommendation/', include('book_recommendation.urls')),
]
