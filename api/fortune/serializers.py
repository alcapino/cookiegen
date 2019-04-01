from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from core.models import FortuneModel


class FortuneSerializer(ModelSerializer):
  def create(self, validated_data):
    new_fortune = FortuneModel(**validated_data)
    new_fortune.save();
    return new_fortune


  class Meta:
    model = FortuneModel
    fields = '__all__'
