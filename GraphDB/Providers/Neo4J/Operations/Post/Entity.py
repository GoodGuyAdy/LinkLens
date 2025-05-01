from GraphDB.Providers.Neo4J.NeoModels.Entity import EntityNode


def create_or_update_entity_node(entity_obj):
    """Creates a Entity type node in neo4j from Entity model obj"""
    entity_node_obj = EntityNode.nodes.get_or_none(entity_id=entity_obj.entity_id)

    if entity_node_obj:
        entity_node_obj.entity_id = entity_obj.entity_id
        entity_node_obj.entity_name = entity_obj.entity_name
        entity_node_obj.entity_type = entity_obj.entity_type
        entity_node_obj.save()
    else:
        EntityNode(
            entity_id=entity_obj.entity_id,
            entity_name=entity_obj.entity_name,
            entity_type=entity_obj.entity_type,
        ).save()
