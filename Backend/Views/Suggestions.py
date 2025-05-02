from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Suggestions import SuggestionsGetSerializer
from Core.GetOperations.Suggestions import get_ai_suggestion
from Backend.Serializers.Error.FlatError import serializer_errors


class SuggestionsClass(APIView):
    """
    Suggestions Class
    """

    def get(self, request):
        """
        Suggestions GET Method
        """

        data = {
            "username": request.GET.get("username"),
            "entity_type": request.GET.get("entity_type"),
        }
        serializer = SuggestionsGetSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            entity_type = serializer.validated_data["entity_type"]

            response_data = get_ai_suggestion(username, entity_type)

            return Response(
                status=200,
                data={"Data": response_data},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
