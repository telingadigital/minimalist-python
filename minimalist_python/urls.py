"""minimalist_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Core Import
from django.contrib import admin
from django.urls import path

# Route Import
from . import views as front_views

urlpatterns = [
	# Front Route
	path('', front_views.index),
	path('about/', front_views.about),
	path('contact/', front_views.contact),
	path('blog/', front_views.blog),

	# Back Route
    path('admin/', admin.site.urls),
]
