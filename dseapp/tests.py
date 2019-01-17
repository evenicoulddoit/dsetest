# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from dseapp.models import Parent, ParentSerializer


class TestModels(TestCase):
    def test(self):
        parent = Parent.objects.create()

        ParentSerializer(parent).data


