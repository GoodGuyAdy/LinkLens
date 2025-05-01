from Models.Event import Event
from Core.DatabaseOperation.User import get_user
from Core.DatabaseOperation.Entity import get_entity


def create_event(user, entity, event_type):
    """
    Creates a new Event in the database.
    """
    event = Event.objects.create(user=user, entity=entity, event_type=event_type)
    return event


def update_event(id, user, entity, event_type):
    """
    Updates an existing Event in the database.
    """
    event = Event.objects.get(id=id)
    event.user = user
    event.entity = entity
    event.event_type = event_type
    event.save()
    return event


def register_event_function(username, event_type, entity_name, entity_type):
    """
    Create event obj form username and entitiy's type and name
    """

    user_obj = get_user(username=username)
    entity_obj = get_entity(entity_name=entity_name, entity_type=entity_type)

    event_obj = create_event(user=user_obj, entity=entity_obj, event_type=event_type)

    return event_obj
