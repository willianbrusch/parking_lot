from rest_framework import serializers


class VehicleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    vehicle_type = serializers.CharField()
    license_plate = serializers.CharField()
    arrived_at = serializers.DateTimeField(required=False)
    paid_at = serializers.DateTimeField(required=False)
    amount_paid = serializers.IntegerField(required=False)
    variety = serializers.CharField(max_length=255, required=False)
    level_name = serializers.CharField(max_length=255, required=False)
    level_id = serializers.IntegerField(required=False)
