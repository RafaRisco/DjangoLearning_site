from rest_framework import serializers
from . import models

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
