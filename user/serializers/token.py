from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        user = User.objects.get(id=user.id)
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = user.username
        token['role'] = user.role

        return token