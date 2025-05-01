from GraphDB.Providers.Neo4J.NeoModels.User import UserNode


def delete_user_node(user_obj):
    """Deletes a User type node from Neo4j by user_id"""
    user_node_obj = UserNode.nodes.get_or_none(user_id=user_obj.user_id)

    if user_node_obj:
        user_node_obj.delete()
        return True
    else:
        return False
