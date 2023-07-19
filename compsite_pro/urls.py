from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    #homepage
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('about',views.about,name='about'),
    path('coming',views.coming,name='coming'),
    path('Subjects',views.topics,name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    ] 
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)