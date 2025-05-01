from GraphDB.Providers.Neo4J.NeoModels.User import UserNode


def create_or_update_user_node(user_obj):
    """Creates a User type node in neo4j from User model obj"""
    user_node_obj = UserNode.nodes.get_or_none(user_id=user_obj.user_id)

    print("Creating user node")

    if user_node_obj:
        user_node_obj.user_id = user_obj.user_id
        user_node_obj.username = user_obj.username
        user_node_obj.save()
    else:
        UserNode(
            user_id=user_obj.user_id,
            username=user_obj.username,
        ).save()
