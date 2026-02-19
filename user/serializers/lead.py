from rest_framework import serializers

from user.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

    def update(self, instance, validated_data):
        instance = super(LeadSerializer, self).update(instance, validated_data)
        instance.save()
        return instance
