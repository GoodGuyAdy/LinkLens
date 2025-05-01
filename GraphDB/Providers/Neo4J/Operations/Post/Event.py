from GraphDB.Providers.Neo4J.NeoModels.Entity import EntityNode
from GraphDB.Providers.Neo4J.NeoModels.User import UserNode
from Models.Event import Event


def register_event_relation(event_obj):
    """Creates a relation in neo4j form user node to entity node based on provided event obj"""
    user_node = UserNode.nodes.get(user_id=event_obj.user.user_id)
    entity_node = EntityNode.nodes.get(entity_id=event_obj.entity.entity_id)

    if event_obj.event_type == Event.EventType.LIKED:
        user_node.liked.connect(entity_node)
    elif event_obj.event_type == Event.EventType.VIEWED:
        user_node.viewed.connect(entity_node)
    elif event_obj.event_type == Event.EventType.HATED:
        user_node.hated.connect(entity_node)
    elif event_obj.event_type == Event.EventType.FOLLOWED:
        user_node.followed.connect(entity_node)
    elif event_obj.event_type == Event.EventType.BLOCKED:
        user_node.blocked.connect(entity_node)
    else:
        raise ValueError("Unsupported relationship!")
