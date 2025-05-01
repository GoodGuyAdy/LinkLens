from GraphDB.Providers.Neo4J.NeoModels.Entity import EntityNode


def delete_entity_node(entity_obj):
    """Deletes an Entity type node from Neo4j by entity_id"""
    entity_node_obj = EntityNode.nodes.get_or_none(entity_id=entity_obj.entity_id)

    if entity_node_obj:
        entity_node_obj.delete()
        return True
    else:
        return False
