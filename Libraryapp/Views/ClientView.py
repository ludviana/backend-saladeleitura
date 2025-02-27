from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Serializers.ClientSerializer import ClientRegisterSerializer, ClientGetSerializer
from Libraryapp.Code.ClientViewCode import (
    register_new_client,
    delete_client,
    update_client,
)
from Libraryapp.utils.functions import log_print
from Libraryapp.models import Client
import json


class GetAllView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            log_print("retornando todos os clientes")
            clients = Client.objects.all()

            list_clients = []

            for result in clients:
                print(result)
                list_clients.append(ClientGetSerializer(result).data) 

            return JsonResponse({
                "data": list_clients
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    


class GetClientByIdView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            log_print("Buscando cliente por id")
            client = Client.objects.get(id=pk)
            
            data = ClientGetSerializer(client).data

            return JsonResponse({
                "data": data
            }, status=HTTPStatus.OK)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)    



class RegisterView(GenericAPIView):
    """ Esse endpoint faz o registro de um novo cliente no banco"""
    serializer_class = ClientRegisterSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            register = register_new_client(request_data)

            if register:
                return JsonResponse({
                    "message": "Cliente Cadastrado",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar cliente",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta um cliente no banco pelo seu id"""
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            register_deleted = delete_client(pk)

            if register_deleted:
                return JsonResponse({
                    "message": "Cliente Deletado",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao deletar cliente",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de um cliente no banco pelo seu id"""
    serializer_class = ClientRegisterSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            name = request_data.get("name")
            phone = request_data.get("phone")
            address = request_data.get("address")

            register_update = update_client(
                pk,
                name,
                phone,
                address,
            )

            if register_update:
                return JsonResponse({
                    "message": "Cliente Atualizado",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao Atualizar o cliente",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
