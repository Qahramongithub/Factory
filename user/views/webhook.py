from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers.webhook import (
    InstagramLeadSerializer,
    TelegramLeadSerializer,
    FacebookLeadSerializer
)


@extend_schema(
    tags=['webhook'],
)
class InstagramLeadView(GenericAPIView):
    serializer_class = InstagramLeadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()
        return Response({"lead_id": lead.id}, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=['webhook'],
)
class TelegramLeadView(GenericAPIView):
    serializer_class = TelegramLeadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()
        return Response({"lead_id": lead.id}, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=['webhook'],
)
class FacebookLeadView(GenericAPIView):
    serializer_class = FacebookLeadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()
        return Response({"lead_id": lead.id}, status=status.HTTP_201_CREATED)
