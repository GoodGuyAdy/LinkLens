from rest_framework import serializers
from Core.DatabaseOperation.User import check_user


class SuggestionsGetSerializer(serializers.Serializer):
    """Serializer to get suggestions based on user and entity_type"""

    username = serializers.CharField(allow_null=False)
    entity_type = serializers.CharField(allow_null=False)

    def validate(self, data):
        username = data["username"]

        user_exists = check_user(username=username)

        if not user_exists:
            raise serializers.ValidationError(
                "User with this username does not exists."
            )

        return data
