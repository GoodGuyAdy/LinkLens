from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Event import (
    EventPostSerializer,
    EventModelSerializer,
)
from Core.DatabaseOperation.Event import register_event_function
from Backend.Serializers.Error.FlatError import serializer_errors


class EventClass(APIView):
    """
    Event Class
    """

    def post(self, request):
        """
        Event Upload Method
        """

        data = {
            "username": request.data.get("username"),
            "event_type": request.data.get("event_type"),
            "entity_name": request.data.get("entity_name"),
            "entity_type": request.data.get("entity_type"),
        }
        serializer = EventPostSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            event_type = serializer.validated_data["event_type"]
            entity_name = serializer.validated_data["entity_name"]
            entity_type = serializer.validated_data["entity_type"]
            event_obj = register_event_function(
                username=username,
                event_type=event_type,
                entity_name=entity_name,
                entity_type=entity_type,
            )

            serializer = EventModelSerializer(event_obj, many=False)

            return Response(
                status=200,
                data=serializer.data,
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
