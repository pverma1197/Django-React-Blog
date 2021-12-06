from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    path('sample/', HelloView.as_view(), name='sample'),
    path('register/', UserRegister.as_view(), name='userdata'),
    path('create_blog/', CreateBlog.as_view(), name='create_blog'),
    path('get_blog/', GetBlog.as_view(), name='get_blog'),
    path('blog_list/<int:id>/', BlogList.as_view(), name='blog_list'),
    path('blog/<uuid:uuid>/', BlogView.as_view(), name='blog'),
    path('tag/<str:tag>/', Tag.as_view(), name='tag'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)