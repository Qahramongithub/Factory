from rest_framework import serializers
from user.models import Lead, LeadSourceMapping, Status, User


# ============================= Base Serializer =============================

class BaseLeadSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    def validate_company_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User not found")
        return value


# ============================= Instagram ===================================

class InstagramLeadSerializer(BaseLeadSerializer):
    leadgen_id = serializers.CharField()

    def create(self, validated_data):
        leadgen_id = validated_data.pop("leadgen_id")
        user_id = validated_data.pop("company_id")

        user = User.objects.get(id=user_id)
        lead_status = Status.objects.get(name="NEW")

        source_mapping, _ = LeadSourceMapping.objects.get_or_create(
            platform="instagram",
            source_id=leadgen_id,
            user=user
        )

        lead = Lead.objects.create(
            status=lead_status,
            source=source_mapping,
            user=user,
            **validated_data
        )

        return lead


# ============================= Telegram ====================================

class TelegramLeadSerializer(BaseLeadSerializer):
    telegram_user_id = serializers.CharField()

    def create(self, validated_data):
        telegram_user_id = validated_data.pop("telegram_user_id")
        user_id = validated_data.pop("company_id")

        user = User.objects.get(id=user_id)
        lead_status = Status.objects.get(name="NEW")

        source_mapping, _ = LeadSourceMapping.objects.get_or_create(
            platform="telegram",
            source_id=telegram_user_id,
            user=user
        )

        lead = Lead.objects.create(
            status=lead_status,
            source=source_mapping,
            user=user,
            **validated_data
        )

        return lead


# ============================= Facebook ====================================

class FacebookLeadSerializer(BaseLeadSerializer):
    leadgen_id = serializers.CharField()

    def create(self, validated_data):
        leadgen_id = validated_data.pop("leadgen_id")
        user_id = validated_data.pop("company_id")

        user = User.objects.get(id=user_id)
        lead_status = Status.objects.get(name="NEW")

        source_mapping, _ = LeadSourceMapping.objects.get_or_create(
            platform="facebook",
            source_id=leadgen_id,
            user=user
        )

        lead = Lead.objects.create(
            status=lead_status,
            source=source_mapping,
            user=user,
            **validated_data
        )

        return lead