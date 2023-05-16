import imp

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (DetailUpdateDeleteTarefa, ListCreateTarefa, UserSignup)

urlpatterns = [
    path('signup', UserSignup.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('tarefas', ListCreateTarefa.as_view(), name='tarefas'),
    path('tarefas/<int:pk>', DetailUpdateDeleteTarefa.as_view(), name='detail-update-delete-tarefa'),

]