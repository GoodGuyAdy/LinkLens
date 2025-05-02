from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.Chat import DatabaseChatSerializer
from Core.GetOperations.Chat import chat_to_data
from Backend.Serializers.Error.FlatError import serializer_errors


class DatabaseChatClass(APIView):
    """
    Database Chat Class
    """

    def get(self, request):
        """
        Database Chat GET Method
        """

        data = {
            "query": request.GET.get("query"),
        }
        serializer = DatabaseChatSerializer(data=data)

        if serializer.is_valid():
            query = serializer.validated_data["query"]

            response_data = chat_to_data(query)

            return Response(
                status=200,
                data={"Data": response_data},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
