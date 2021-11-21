from rest_framework import serializers
from .models import CityWeatherModel


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeatherModel
        fields = ('city', 'list')
        depth = 4
        # fields = ('name', 'main', 'day', 'max', 'min', 'description', 'humidity')
        # depth = 4

# class TemperatureSerializer(serializers.Serializer):
#     day = serializers.FloatField()
#     max = serializers.FloatField()
#     min = serializers.FloatField()
#
# class WeatherDetailSerilizer(serializers.Serializer):
#     main = serializers.CharField(max_length=50)
#     description = serializers.CharField(max_length=100)
#     # icon =
#
# class ListItemSerilizer(serializers.Serializer):
#     weather = WeatherDetailSerilizer(many=True)
#     temp = TemperatureSerializer()
#     # dt = serializers.DateTimeField()
#     humidity = serializers.FloatField()
#
# class CitySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, default="Enter in the city name")
#
# class WeatherSerializer(serializers.Serializer):
#     city = CitySerializer()
#     list = ListItemSerilizer(many=True)
