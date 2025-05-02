from rest_framework import serializers


class DatabaseChatSerializer(serializers.Serializer):
    """Serializer to chat with the data by giving query"""

    query = serializers.CharField(allow_null=False)

    def validate(self, data):
        return data
