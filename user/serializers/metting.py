from rest_framework import serializers

from user.models import Meeting
class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
        read_only_fields = ('id',)
    def create(self, validated_data):
        pass

