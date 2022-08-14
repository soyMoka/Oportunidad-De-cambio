from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrarUsuarios

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('agregar/', RegistrarUsuarios.as_view() ,name="agregar"),
    # path('modificarUsuario/<str:pk>', ModificarUsuario.as_view() ,name="modificarUsuario"),
    # path('eliminarUsuario/<int:pk>', DeleteUsuario.as_view() ,name="eliminarUsuario")
]