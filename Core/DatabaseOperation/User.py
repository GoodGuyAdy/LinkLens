from Models.User import User


def check_user(username=None, user_id=None):
    """
    Checks if a user is present in the database by username or user_id.
    At least one parameter must be provided.
    """
    if username:
        return User.objects.filter(username=username).exists()
    elif user_id:
        return User.objects.filter(user_id=user_id).exists()
    else:
        raise ValueError("You must provide either 'username' or 'user_id'")


def get_user(username):
    """
    Creates a new user in the database.
    """
    user_obj = User.objects.get(username=username)
    return user_obj

def filter_user(**kwargs):
    """
    Creates a new user in the database.
    """
    user_obj_qs = User.objects.filter(**kwargs)
    return user_obj_qs


def create_user(username, email, first_name, last_name):
    """
    Creates a new user in the database.
    """
    user_obj = User.objects.create(
        username=username, email=email, first_name=first_name, last_name=last_name
    )
    return user_obj


def update_user(user_id, username, email, first_name, last_name):
    """
    Updates an existing user in the database.
    """
    user_obj = User.objects.get(user_id=user_id)
    user_obj.username = username
    user_obj.email = email
    user_obj.first_name = first_name
    user_obj.last_name = last_name
    user_obj.save()
    return user_obj


def delete_user(user_id):
    """
    Deletes a user from the database
    """
    User.objects.filter(user_id=user_id).delete()
