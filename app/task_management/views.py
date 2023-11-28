from rest_framework import viewsets, pagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters

from .serializers import TaskSerializer
from .models import Task


class TaskPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        queryset = queryset.order_by('id')
        return super().paginate_queryset(queryset, request, view)


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'created_at']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = [filters.DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
