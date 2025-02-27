from django.http import JsonResponse
from http import HTTPStatus
from rest_framework.generics import GenericAPIView
from Libraryapp.Code.LibraryViewCode import ( 
    verify_if_email_and_password_is_correct,
    register_new_library,
    delete_library,
    update_library,
)
from Libraryapp.Serializers.LibrarySerializer import (
    LibraryLoginSerializer,
    LibraryRegisterSerializer,
    LibraryDeleteSerializer,
    
)

class LoginView(GenericAPIView): 
    """Esse endpoint busca uma biblioteca no banco para fazer login"""
    serializer_class = LibraryLoginSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            email = request_data.get("email")
            user_password = request_data.get("password")

            verify_user = verify_if_email_and_password_is_correct(email, user_password)

            if(verify_user):
                return JsonResponse({
                    "message": "Ok",
                }, status=HTTPStatus.OK)    
            else:
                return JsonResponse({
                    "message": "email ou senha incorreto",
                }, status=HTTPStatus.UNAUTHORIZED)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class RegisterView(GenericAPIView):
    """ Esse endpoint faz o registro de uma nova biblioteca no banco"""
    serializer_class = LibraryRegisterSerializer
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            register = register_new_library(request_data)

            if register:
                return JsonResponse({
                    "message": "Biblioteca Cadastrada",
                }, status=HTTPStatus.CREATED)
            
            return JsonResponse({
                    "message": "Erro ao cadastrar biblioteca",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
        

class DeleteView(GenericAPIView):
    """ Esse endpoint deleta uma biblioteca no banco pelo seu id"""
    serializer_class = LibraryDeleteSerializer
    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            register_deleted = delete_library(pk)

            if register_deleted:
                return JsonResponse({
                    "message": "Biblioteca Deletada",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao deletar biblioteca",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)

class UpdateView(GenericAPIView):
    """ Esse endpoint atualiza dados de uma biblioteca no banco"""
    serializer_class = LibraryRegisterSerializer
    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            request_data = request.data

            name = request_data.get("email")
            address = request_data.get("password")
            email = request_data.get("email")
            password = request_data.get("password")

            register_update = update_library(
                pk,
                name,
                address,
                email,
                password
            )

            if register_update:
                return JsonResponse({
                    "message": "Biblioteca Atualizada",
                }, status=HTTPStatus.OK)
            
            return JsonResponse({
                    "message": "Erro ao Atualizar a biblioteca",
                }, status=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "message": "Ocorreu um erro inesperado",
                "exception_name": type(e).__name__,
                "exception_args": e.args
            }, status=HTTPStatus.BAD_REQUEST)
