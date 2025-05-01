from rest_framework import serializers
from Core.DatabaseOperation.User import check_user, get_user
from Models.User import User


class UserModelSerializer(serializers.ModelSerializer):
    """This contains serializers to get a User from User model"""

    class Meta:
        model = User
        fields = "__all__"


class UserGetSerializer(serializers.Serializer):
    """This contains serializers to get a User"""

    username = serializers.CharField(allow_null=True)

    def validate(self, data):
        username = data["username"]

        if username:
            user_exists = check_user(username)

            if not user_exists:
                raise serializers.ValidationError(
                    "User with this username does not exists."
                )

        return data


class UserPostSerializer(serializers.Serializer):
    """This contains serializers to post a User"""

    username = serializers.CharField(allow_null=False)
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)

    def validate(self, data):
        username = data["username"]

        user_exists = check_user(username)

        if user_exists:
            raise serializers.ValidationError("User with this username already exists.")

        return data


class UserPutSerializer(serializers.Serializer):
    """This contains serializers to update a User"""

    user_id = serializers.IntegerField(allow_null=False)
    username = serializers.CharField(allow_null=False)
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    first_name = serializers.CharField(allow_null=False)
    last_name = serializers.CharField(allow_null=False)

    def validate(self, data):
        user_id = data["user_id"]
        username = data["username"]

        userid_exists = check_user(user_id=user_id)

        if not userid_exists:
            raise serializers.ValidationError("User with this user_id does not exists.")

        username_exists = check_user(username=username)

        if username_exists:
            user_obj = get_user(username=username)
            if user_obj.user_id != user_id:
                raise serializers.ValidationError(
                    "User with this username already exists."
                )

        return data


class UserDeleteSerializer(serializers.Serializer):
    """This contains serializers to delete a User"""

    user_id = serializers.IntegerField(allow_null=False)

    def validate(self, data):
        user_id = data["user_id"]

        user_exists = check_user(user_id=user_id)

        if not user_exists:
            raise serializers.ValidationError("User with this user_id does not exists.")

        return data
