from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Entity import (
    EntityPostSerializer,
    EntityPutSerializer,
    EntityDeleteSerializer,
    EntityGetSerializer,
    EntityModelSerializer,
)
from Core.DatabaseOperation.Entity import (
    create_entity,
    update_entity,
    delete_entity,
    get_entities,
)
from Backend.Serializers.Error.FlatError import serializer_errors


class EntityClass(APIView):
    """
    Entity Class
    """

    def get(self, request):
        """
        Entity Get Method
        """

        data = {
            "entity_type": request.GET.get("entity_type"),
            "entity_name": request.GET.get("entity_name"),
        }
        serializer = EntityGetSerializer(data=data)

        if serializer.is_valid():
            filters = {}

            if serializer.validated_data.get("entity_type"):
                filters["entity_type"] = serializer.validated_data["entity_type"]
            if serializer.validated_data.get("entity_name"):
                filters["entity_name"] = serializer.validated_data["entity_name"]

            entity_qs = get_entities(**filters)

            serializer = EntityModelSerializer(entity_qs, many=True)

            return Response(
                status=200,
                data=serializer.data,
            )

        return Response(
            status=400,
            data={"Message": serializer_errors(serializer.errors)},
        )

    def post(self, request):
        """
        Entity Create Method
        """
        data = {
            "entity_type": request.data.get("entity_type"),
            "entity_name": request.data.get("entity_name"),
            "description": request.data.get("description"),
        }
        serializer = EntityPostSerializer(data=data)

        if serializer.is_valid():
            entity_type = serializer.validated_data["entity_type"]
            entity_name = serializer.validated_data["entity_name"]
            description = serializer.validated_data["description"]
            entity_obj = create_entity(entity_type, entity_name, description)

            serializer = EntityModelSerializer(entity_obj)

            return Response(status=200, data=serializer.data)
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def put(self, request):
        """
        Entity Update Method
        """
        data = {
            "entity_id": request.data.get("entity_id"),
            "entity_type": request.data.get("entity_type"),
            "entity_name": request.data.get("entity_name"),
            "description": request.data.get("description"),
        }
        serializer = EntityPutSerializer(data=data)

        if serializer.is_valid():
            entity_id = serializer.validated_data["entity_id"]
            entity_type = serializer.validated_data["entity_type"]
            entity_name = serializer.validated_data["entity_name"]
            description = serializer.validated_data["description"]
            update_entity(entity_id, entity_type, entity_name, description)
            return Response(
                status=200,
                data={"Message": "Entity Updated"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def delete(self, request):
        """
        Entity Delete Method
        """
        data = {
            "entity_id": request.GET.get("entity_id"),
        }
        serializer = EntityDeleteSerializer(data=data)

        if serializer.is_valid():
            entity_id = serializer.validated_data["entity_id"]
            delete_entity(entity_id)
            return Response(
                status=200,
                data={"Message": "Entity Deleted"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
