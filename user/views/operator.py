from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User
from user.serializers.operator import OperatorSerializer


@extend_schema(
    tags=['operator'],
)
class OperatorCreateAPIVieW(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = (IsAuthenticated,)


@extend_schema(
    tags=['operator'],
)
class OperatorListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        user = self.request.user.id
        queryset = User.objects.filter(user_id=user).all()
        return queryset


@extend_schema(
    tags=['operator'],
)
class OperatorUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user.id
        operator_id = self.kwargs.get('pk')
        queryset = User.objects.filter(user_id=user, id=operator_id).first()
        return queryset


@extend_schema(
    tags=['operator'],
)
class OperatorDeleteAPIView(DestroyAPIView):
    serializer_class = OperatorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        operator_id = self.kwargs.get('pk')
        queryset = User.objects.filter(user_id=user, id=operator_id)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return queryset
