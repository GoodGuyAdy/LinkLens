import datetime
from GraphDB.Providers.Neo4J.NeoModels.Entity import EntityNode
from neomodel import (
    StructuredNode,
    StringProperty,
    RelationshipTo,
    DateTimeProperty,
    StructuredRel,
    IntegerProperty,
)


class InteractionRel(StructuredRel):
    timestamp = DateTimeProperty(default=datetime.datetime.now)


class UserNode(StructuredNode):
    user_id = IntegerProperty()
    username = StringProperty()

    liked = RelationshipTo("EntityNode", "LIKED", model=InteractionRel)
    viewed = RelationshipTo("EntityNode", "VIEWED", model=InteractionRel)
    followed = RelationshipTo("EntityNode", "FOLLOWED", model=InteractionRel)
    blocked = RelationshipTo("EntityNode", "BLOCKED", model=InteractionRel)
    disliked = RelationshipTo("EntityNode", "DISLIKED", model=InteractionRel)
