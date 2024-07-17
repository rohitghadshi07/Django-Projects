from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.add_emp,name='add_emp'),
    path('delete_emp/<int:emp_id>/',views.delete_emp,name='delete_emp'),
    path('update_emp/<int:emp_id>/',views.update_emp,name="update_emp"),
    path('do_update_emp/<int:emp_id>/',views.do_update_emp,name="do_update_emp"),
    path('gallery/',views.gallery,name="gallery"),
    path('view/',views.view_emp),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
