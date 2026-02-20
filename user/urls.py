from django.urls import path
from django.urls import path
from user.views.webhook import InstagramLeadView, TelegramLeadView, FacebookLeadView

from user.views.lead import OperatorLeadListView, UserLeadListView, UserLeadUpdateView
from user.views.operator import OperatorListAPIView, OperatorUpdateAPIView, OperatorCreateAPIVieW, OperatorDeleteAPIView
from user.views.token import MyTokenObtainSlidingView
from rest_framework_simplejwt.views import (
    TokenRefreshSlidingView, TokenBlacklistView,
)

# =========================== Auth ============================================================
urlpatterns = [

    path('api/token/', MyTokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

]

# =========================== Operator CRUD =======================================================
urlpatterns += [
    path('api/opertor/create', OperatorCreateAPIVieW.as_view(), name='operator_create'),
    path('api/opertor/list', OperatorListAPIView.as_view(), name='operator_list'),
    path('api/opertor/update/<int:pk>', OperatorUpdateAPIView.as_view(), name='operator_update'),
    path('api/operator/delete/<int:pk>', OperatorDeleteAPIView.as_view(), name='operator_delete'),
]

# ========================================== Lead Operator RU =======================================
urlpatterns += [
    path('api/opertor/lead/list', OperatorLeadListView.as_view(), name='operator_lead_list'),
    path('api/api/opertor/lead/update/<int:pk>', OperatorUpdateAPIView.as_view(), name='operator_lead_update'),

]

# ============================================== Lead User RUD ============================
urlpatterns += [
    # path('api/lead/create',),
    path('api/user/lead/list', UserLeadListView.as_view(), name='user_lead_list'),
    path('api/user/lead/update/<int:pk>', UserLeadUpdateView.as_view(), name='user_lead_update'),

]

# urls.py
# ================================= Webhook ===================================================
urlpatterns += [
    path("webhook/instagram/", InstagramLeadView.as_view(), name="instagram"),
    path("webhook/telegram/", TelegramLeadView.as_view(), name="telegram"),
    path("webhook/facebook/", FacebookLeadView.as_view(), name="facebook"),
]

