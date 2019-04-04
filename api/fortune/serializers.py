from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from core.models import FortuneModel


class FortuneSerializer(ModelSerializer):
  def create(self, validated_data):
    new_fortune = FortuneModel(**validated_data)
    new_fortune.save();
    return new_fortune

  def update(self, instance, validated_data):
    instance.text = validated_data.get('text', instance.text)
    instance.save()
    return instance


  class Meta:
    model = FortuneModel
    fields = '__all__'
