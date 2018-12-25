import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class LimitedModelSerializer(ModelSerializer):
    """Allows a serializer to remove some fields based on whether
    a user is a staff member or not, or whether the user owns a certain object"""
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if not (request != None and (request.user.is_staff or self.user_is_owner())):
            allowed_to_all = set(self.allowed_to_all)
            extra_fields = set(self.fields) - allowed_to_all
            for field in extra_fields:
                representation.pop(field)
        return representation

    def user_is_owner(self):
        request = self.context.get('request')
        try:
            if request.user.profile.id == self.instance.id:
                return True
            else:
                return False
        except AttributeError:
            return False


class Base64ImageField(serializers.ImageField):
    """Defines a base64image serializer field that should be used to
    recieve images as base64 encoded data"""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            img_format, img_str = data.split(';base64,')
            extension = img_format.split('/')[-1]
            extension = 'jpg' if extension == 'jpeg' else extension
            img_id = uuid.uuid4()
            data = ContentFile(base64.b64decode(img_str), name='.'.join((img_id.urn[9:], extension)))
        return super().to_internal_value(data)