from rest_framework_simplejwt.views import TokenObtainSlidingView

from user.serializers.token import MyTokenObtainPairSerializer


class MyTokenObtainSlidingView(TokenObtainSlidingView):
    serializer_class = MyTokenObtainPairSerializer