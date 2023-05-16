from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView




from api.models import Tarefa
from api.serializers import TarefaSerializer, UserSerializer


class ListCreateTarefa(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        tarefas = Tarefa.objects.filter(usuario=request.user)
        serializer = TarefaSerializer(tarefas, many=True)
        context = {
            'tarefas': serializer.data,
        }
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailUpdateDeleteTarefa(APIView):

    permission_classes = [IsAuthenticated]

    def get_tarefa(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            raise Http404
        
   
    def get(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        return Response(serializer.data)
    

    def put(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def usuario_permission(self, request, target):
        if target.usuario != request.user:
            self.permission_denied(request, message='Permissão negada!')
    
class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)