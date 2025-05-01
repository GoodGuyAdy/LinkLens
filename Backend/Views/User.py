from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.Serializers.User import (
    UserPostSerializer,
    UserDeleteSerializer,
    UserPutSerializer,
    UserGetSerializer,
    UserModelSerializer,
)
from Core.DatabaseOperation.User import (
    delete_user,
    create_user,
    update_user,
    get_user,
    filter_user,
)
from Backend.Serializers.Error.FlatError import serializer_errors


class UserClass(APIView):
    """
    User Class
    """

    def get(self, request):
        """
        User Get Method
        """

        data = {
            "username": request.GET.get("username"),
        }
        serializer = UserGetSerializer(data=data)

        if serializer.is_valid():
            filters = {}
            if serializer.validated_data["username"]:
                filters["username"] = serializer.validated_data["username"]

            user_obj_qs = filter_user(**filters)

            serializer = UserModelSerializer(user_obj_qs, many=True)

            return Response(
                status=200,
                data=serializer.data,
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def post(self, request):
        """
        User Upload Method
        """

        print(request.data)

        data = {
            "username": request.data.get("username"),
            "email": request.data.get("email"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
        }

        print(data)
        serializer = UserPostSerializer(data=data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]
            user_obj = create_user(username, email, first_name, last_name)

            serializer = UserModelSerializer(user_obj)

            return Response(
                status=200,
                data=serializer.data,
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def put(self, request):
        """
        User Update Method
        """

        data = {
            "user_id": request.data.get("user_id"),
            "username": request.data.get("username"),
            "email": request.data.get("email"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
        }
        serializer = UserPutSerializer(data=data)

        if serializer.is_valid():
            user_id = serializer.validated_data["user_id"]
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            first_name = serializer.validated_data["first_name"]
            last_name = serializer.validated_data["last_name"]
            update_user(user_id, username, email, first_name, last_name)
            return Response(
                status=200,
                data={"Message": "User Updated"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )

    def delete(self, request):
        """
        User Delete Method
        """

        data = {
            "user_id": request.GET.get("user_id"),
        }
        serializer = UserDeleteSerializer(data=data)

        if serializer.is_valid():
            user_id = serializer.validated_data["user_id"]
            delete_user(user_id)
            return Response(
                status=200,
                data={"Message": "User Deleted"},
            )
        else:
            return Response(
                status=400,
                data={"Message": serializer_errors(serializer.errors)},
            )
