# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from rest_framework.serializers import ModelSerializer
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class Parent(models.Model):
    pass


class Child(models.Model):
    parent = models.OneToOneField(Parent)


class ChildSerializer(SerializerExtensionsMixin, ModelSerializer):
    class Meta:
        model = Child
        fields = ('id',)


class ParentSerializer(SerializerExtensionsMixin, ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id',)
        expandable_fields = dict(
            child=dict(
                serializer=ChildSerializer,
                id_source='child.id'
            ))


class VanillaParentSerializer(ModelSerializer):
    child_id = PrimaryKeyRelatedField(
        source='child.id',
        queryset=Child.objects.all(),
        allow_null=True,
    )

    class Meta:
        model = Parent
        fields = ('id','child_id')
