from django.forms import widgets
from rest_framework import serializers

from api.models import Task


class TaskSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(widget=widgets.Textarea,
                                        max_length=100000,
                                        required=False)
    user = serializers.Field()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            for attr in ['pk', 'title', 'description', 'user']:
                setattr(instance, attr, attrs.get(attr))
            return instance

        # Create new instance
        return Task(**attrs)