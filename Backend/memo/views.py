from django.shortcuts import render
from .models import Memo, Result, Character
from .serializers import MemoSrializer, ResultSrializer, CharacterSrializer
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class MemoView(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    
    serializer_class = MemoSrializer
    queryset = Memo.objects.all()

    def list(self, request):
        queryset = Memo.objects.all()
        serializer = MemoSrializer(queryset,  many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = {'result_id':request.data['result'],
                     'my_chara_id': request.data['my_chara'], 
                     'op_chara_id':request.data['op_chara'], 
                     'date':request.data['date'],
                     'time':request.data['time']}
            serializer = MemoSrializer(data=data)
            serializer.is_valid()
            serializer.save()
            queryset = Memo.objects.all()
            serializer = MemoSrializer(queryset,  many=True)
            return Response(serializer.data)

        except Memo.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except Result.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except Character.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except ValueError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except ValidationError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except AssertionError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        
        

    def update(self, request):
        try:
            instance = Memo.objects.get(pk=request.data['id'])
            data = {'result_id':request.data['result'],
                     'my_chara_id':request.data['my_chara'], 
                     'op_chara_id':request.data['op_chara'], 
                     'date':request.data['date'],
                     'time':request.data['time']}
            serializer = MemoSrializer(instance, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            queryset = Memo.objects.all()
            serializer = MemoSrializer(queryset,  many=True)
            return Response(serializer.data)

        except Memo.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except Result.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except Character.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except ValueError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
        except AssertionError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request):
        try:
            Memo.objects.filter(pk=request.data['id']).delete()
            queryset = Memo.objects.all()
            serializer = MemoSrializer(queryset,  many=True)
            return Response(serializer.data)
        except Memo.DoesNotExist as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)   
        except ValueError as ex:
            return Response(data=ex.args,status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def patch(self, request):
        return self.update(request)

    def put(self, request):
        return self.destroy(request)

class CharaView(generics.ListAPIView):
    serializer_class = CharacterSrializer
    queryset = Character.objects.all()

class ResultView(generics.ListAPIView):
    serializer_class = ResultSrializer
    queryset = Result.objects.all()


    



