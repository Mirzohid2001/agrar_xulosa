from rest_framework import serializers
from .models import Region, Seed, Fertiliser,Tractor,Worker,WorkType,Order,News,Review,Banner,Statistic


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = ('id', 'place', 'name', 'volume')

class FertiliserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertiliser
        fields = ('id', 'place', 'product', 'azot_kg', 'soil_azot', 'fosfor_kaliy_azotN')


class TractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tractor
        fields = ('id', 'place', 'name', 'power')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'place', 'name', 'power')

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = ('id', 'place', 'name', 'power')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'place', 'seed', 'product', 'fertiliser', 'tractor', 'worker', 'work_type', 'area', 'cost')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content','image')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','user','text','rate')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id','image','text')

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('count', 'created_at', 'updated_at')





