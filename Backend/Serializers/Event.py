from rest_framework import serializers
from Models.Event import Event
from Core.DatabaseOperation.User import check_user
from Core.DatabaseOperation.Entity import check_entity


class EventModelSerializer(serializers.ModelSerializer):
    """This contains serializers to get a Event from Event model"""

    class Meta:
        model = Event
        fields = "__all__"


class EventPostSerializer(serializers.Serializer):
    """Serializer to create an Event"""
    username = serializers.CharField(allow_null=False)
    event_type = serializers.CharField(allow_null=False)
    entity_name = serializers.CharField(allow_null=False)
    entity_type = serializers.CharField(allow_null=False)

    def validate_event_type(self, value):
        valid_choices = [choice[0] for choice in Event.EventType.choices]
        if value not in valid_choices:
            raise serializers.ValidationError(
                f"Invalid event_type '{value}'. Valid choices are: {', '.join(valid_choices)}."
            )
        return value

    def validate(self, data):
        username = data["username"]
        entity_type = data["entity_type"]
        entity_name = data["entity_name"]

        user_exists = check_user(username=username)

        if not user_exists:
            raise serializers.ValidationError(
                "User with this username does not exists."
            )

        entity_exists = check_entity(entity_type=entity_type, entity_name=entity_name)

        if not entity_exists:
            raise serializers.ValidationError(
                "Entity with this type and name does not exists."
            )

        return data
