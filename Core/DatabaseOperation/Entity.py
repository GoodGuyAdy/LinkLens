from Models.Entity import Entity


def check_entity(entity_type=None, entity_name=None, entity_id=None):
    """
    Checks if an Entity is present in the database by type and name, or by entity_id.
    At least one method of identification must be provided.
    """
    if entity_id:
        return Entity.objects.filter(entity_id=entity_id).exists()
    elif entity_type and entity_name:
        return Entity.objects.filter(
            entity_type=entity_type, entity_name=entity_name
        ).exists()
    else:
        raise ValueError(
            "You must provide either 'entity_id' or both 'entity_type' and 'entity_name'"
        )


def get_entity(entity_type, entity_name):
    """
    Gets a Entity from the database
    """
    entity_obj = Entity.objects.get(entity_type=entity_type, entity_name=entity_name)
    return entity_obj


def create_entity(entity_type, entity_name, description):
    """
    Creates a new Entity in the database.
    """
    entity = Entity.objects.create(
        entity_type=entity_type, entity_name=entity_name, description=description
    )
    return entity


def update_entity(entity_id, entity_type, entity_name, description):
    """
    Updates an existing Entity in the database.
    """
    entity = Entity.objects.get(entity_id=entity_id)
    entity.entity_type = entity_type
    entity.entity_name = entity_name
    entity.description = description
    entity.save()
    return entity


def delete_entity(entity_id):
    """
    Deletes a entity from the database
    """
    Entity.objects.filter(entity_id=entity_id).delete()


def get_entities(**filters):
    """
    Returns a queryset of Entity objects.
    If no filters are provided, returns all entities.
    Filters must be any valid field(s) of the Entity model.

    Example usage:
    - get_entities()  # returns all entities
    - get_entities(entity_type='Movie')  # filters by entity_type
    - get_entities(entity_name='Matrix', entity_type='Movie')  # multiple filters
    """
    entities_qs = Entity.objects.filter(**filters)
    return entities_qs
