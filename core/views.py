from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import viewsets
from .models import Kategori, Artikel_Kategori, Hasil_Kategori
from .serializers import KategoriSerializer, ArtikelKategoriSerializer, HasilKategoriSerializer
from .utils import get_categories
from django.http import Http404


class KategoriViewSet(viewsets.ViewSet):
    serializer_class = KategoriSerializer

    def list(self, request):
        category_name = request.query_params.get('nama_kategori')
        if category_name:
            page_titles = get_categories(category_name)
            queryset = Kategori.objects.filter(nama_kategori__in=page_titles)
            serializer = KategoriSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ArtikelKategoriViewSet(viewsets.ModelViewSet):
    serializer_class = ArtikelKategoriSerializer

    def get_queryset(self):
        # Get the value of the query parameter 'nama_kategori'
        category_name = self.request.query_params.get('nama_kategori')

        # If 'nama_kategori' is provided, filter the queryset accordingly
        if category_name:
            # Retrieve the Kategori object based on the provided category name
            try:
                kategori = Kategori.objects.get(nama_kategori=category_name)
                queryset = Artikel_Kategori.objects.filter(nama_kategori=kategori)
                return queryset
            except Kategori.DoesNotExist:
                # Raise 404 if the category doesn't exist
                raise Http404("Kategori does not exist")
        else:
            return Artikel_Kategori.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

class HasilKategoriViewSet(viewsets.ModelViewSet):
    serializer_class = HasilKategoriSerializer

    def get_queryset(self):
        # Get the value of the query parameter 'nama_kategori'
        category_name = self.request.query_params.get('nama_kategori')

        # If 'nama_kategori' is provided, filter the queryset accordingly
        if category_name:
            # Retrieve the Kategori object based on the provided category name
            try:
                kategori = Kategori.objects.get(nama_kategori=category_name)
                queryset = Hasil_Kategori.objects.filter(id_kategori=kategori)
                return queryset
            except Kategori.DoesNotExist:
                # Raise 404 if the category doesn't exist
                raise Http404("Kategori does not exist")
        else:
            return Hasil_Kategori.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


