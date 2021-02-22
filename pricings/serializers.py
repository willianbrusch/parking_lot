from rest_framework import serializers


class PriceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    a_coefficient = serializers.IntegerField()
    b_coefficient = serializers.IntegerField()
