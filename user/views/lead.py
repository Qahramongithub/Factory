from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, get_object_or_404, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Lead, User
from user.serializers.lead import LeadSerializer


class LeadCreateAPIView(APIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = LeadSerializer(data=data)
        
#
# ======================= Lead Operator RU ========
@extend_schema(
    tags=['operator_lead'],
)
class OperatorLeadListView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        operator = self.request.user.id
        queryset = Lead.objects.filter(operator=operator).all()
        if not queryset:
            return Lead.objects.none()
        return queryset


@extend_schema(
    tags=['operator_lead'],
)
class OperatorLeadUpdateView(APIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        operator = self.request.user.id
        lead_id = self.kwargs['pk']
        queryset = Lead.objects.filter(operator=operator, id=lead_id).first()
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return queryset


# ======================= User Lead RUD ===============
@extend_schema(
    tags=['user_lead'],
)
class UserLeadListView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        operator = User.objects.filter(user_id=user).all()
        leads = Lead.objects.filter(user_id=operator).all()
        if not leads:
            return Lead.objects.none()
        return leads


@extend_schema(
    tags=['user_lead'],
)
class UserLeadUpdateView(UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user.id
        lead_id = self.kwargs['pk']
        operator = User.objects.filter(user_id=user)
        return get_object_or_404(Lead, id=lead_id, operator=operator)

@extend_schema(tags=['user_lead'])
class UserLeadDeleteView(DestroyAPIView):
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user_id = self.request.user.id
        lead_id = self.kwargs['pk']
        operator_ids = User.objects.filter(user_id=user_id).values_list('id', flat=True)
        return get_object_or_404(Lead, id=lead_id, operator_id__in=operator_ids)
