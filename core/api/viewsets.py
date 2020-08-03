from rest_framework import viewsets, filters
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    search_fields = ['nome', 'descricao', 'endereco__linha1']
    # lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        query_set = PontoTuristico.objects.all()

        if id:
            query_set = query_set.filter(id=id)
        
        if nome:
            query_set = query_set.filter(nome__iexact=nome)

        if descricao:
            query_set = query_set.filter(descricao__iexact=descricao)

        return query_set

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self). destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, *args, **kwargs):
        return super(PontoTuristico, self).partial_update(request, *args, **kwargs)

    

