from neomodel import db


def create_or_update_entity_node(entity_obj):
    """
    Dynamically creates or updates an entity node based on entity_type
    Handles any type of entity with any properties
    """

    entity_id = entity_obj.entity_id
    entity_name = entity_obj.entity_name
    entity_type = entity_obj.entity_type
    description = entity_obj.description

    model_name = f"{entity_type}"

    fields = {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "description": description,
    }

    set_clause = ", ".join(
        [f"n.{field} = '{value}'" for field, value in fields.items()]
    )

    cypher_query = f"""
        MERGE (n:{model_name} {{entity_id: '{entity_id}'}})
        SET {set_clause}
        RETURN n
        """

    db.cypher_query(cypher_query)
