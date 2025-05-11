from neomodel import db


def register_event_relation(event_obj):
    """Creates a relation in neo4j from user node to entity node based on provided event obj"""

    user_id = event_obj.user.user_id
    entity_id = event_obj.entity.entity_id
    entity_type = event_obj.entity.entity_type
    event_type = event_obj.event_type

    relationship_type = event_type.upper()

    cypher_query = f"""
        MATCH (u:UserNode) WHERE u.user_id = {user_id}
        MATCH (e:{entity_type}) WHERE e.entity_id = '{entity_id}'
        CREATE (u)-[r:{relationship_type}]->(e)
        RETURN r
        """

    db.cypher_query(cypher_query)
