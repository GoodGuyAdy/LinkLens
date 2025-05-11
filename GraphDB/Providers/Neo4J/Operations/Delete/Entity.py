from neomodel import db


def delete_entity_node(entity_obj):
    """
    Dynamically deletes an entity node based on entity_type and entity_id
    """
    entity_id = entity_obj.entity_id
    entity_type = entity_obj.entity_type

    model_name = f"{entity_type}"

    cypher_query = f"""
        MATCH (n:{model_name} {{entity_id: '{entity_id}'}})
        DETACH DELETE n
    """

    db.cypher_query(cypher_query)
