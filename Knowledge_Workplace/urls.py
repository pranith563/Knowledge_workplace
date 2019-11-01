"""Knowledge_Workplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
	path('',views.index,name='index'),
	path('<str:repo_name>/',views.load_repo,name='load_repo'),
	path('<str:repo_name>/upload_doc',views.upload_doc,name='upload_doc'),
   	path('<str:repo_name>/upload_entities',views.upload_entities,name='upload_doc'),
    path('<str:repo_name>/upload_dictionaries',views.upload_dictionaries,name='upload_doc'),
   	path('<str:repo_name>/upload_relationTypes',views.upload_relationTypes,name='upload_doc'),
	path('<str:repo_name>/get_docs',views.get_docs,name='upload_doc'),
   	path('<str:repo_name>/get_entities',views.get_entities,name='upload_doc'),
    path('<str:repo_name>/get_dictionaries',views.get_dictionaries,name='upload_doc'),
   	path('<str:repo_name>/get_relationTypes',views.get_relationTypes,name='upload_doc'),   
    path('admin/', admin.site.urls),
    path("knowledge_processing/",include('knowledge_processing.urls'))
]
