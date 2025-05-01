from rest_framework import serializers
from Core.DatabaseOperation.Entity import check_entity, get_entities
from Models.Entity import Entity


class EntityModelSerializer(serializers.ModelSerializer):
    """Serializes full Entity model"""

    class Meta:
        model = Entity
        fields = "__all__"


class EntityGetSerializer(serializers.Serializer):
    """Serializer to get an Entity"""

    entity_type = serializers.CharField(allow_null=True)
    entity_name = serializers.CharField(allow_null=True)

    def validate(self, data):
        entity_type = data["entity_type"]
        entity_name = data["entity_name"]

        if entity_type and entity_name:
            entity_exists = check_entity(
                entity_type=entity_type, entity_name=entity_name
            )

            if not entity_exists:
                raise serializers.ValidationError(
                    "Entity with this type and name does not exist."
                )
        return data


class EntityPostSerializer(serializers.Serializer):
    """Serializer to create an Entity"""

    entity_type = serializers.CharField(allow_null=False)
    entity_name = serializers.CharField(allow_null=False)
    description = serializers.CharField(allow_null=False)

    def validate(self, data):
        entity_type = data["entity_type"]
        entity_name = data["entity_name"]

        entity_exists = check_entity(entity_type=entity_type, entity_name=entity_name)

        if entity_exists:
            raise serializers.ValidationError(
                "Entity with this type and name already exists."
            )
        return data


class EntityPutSerializer(serializers.Serializer):
    """Serializer to update an Entity"""

    entity_id = serializers.IntegerField(allow_null=False)
    entity_type = serializers.CharField(allow_null=False)
    entity_name = serializers.CharField(allow_null=False)
    description = serializers.CharField(allow_null=False)

    def validate(self, data):
        entity_id = data["entity_id"]
        entity_name = data["entity_name"]
        entity_type = data["entity_type"]

        entityid_exists = check_entity(entity_id=entity_id)

        if not entityid_exists:
            raise serializers.ValidationError("Entity with this ID does not exist.")

        duplicate_entity = (
            get_entities(entity_type=entity_type, entity_name=entity_name)
            .exclude(entity_id=entity_id)
            .first()
        )

        if duplicate_entity:
            raise serializers.ValidationError(
                "Another entity with this type and name already exists."
            )

        return data


class EntityDeleteSerializer(serializers.Serializer):
    """Serializer to delete an Entity"""

    entity_id = serializers.IntegerField(allow_null=False)

    def validate(self, data):
        entity_id = data["entity_id"]

        entity_exists = check_entity(entity_id=entity_id)

        if not entity_exists:
            raise serializers.ValidationError("Entity with this ID does not exist.")
        return data
