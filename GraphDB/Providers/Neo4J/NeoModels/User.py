import datetime
from neomodel import (
    StructuredNode,
    StringProperty,
    DateTimeProperty,
    StructuredRel,
    IntegerProperty,
)


class InteractionRel(StructuredRel):
    timestamp = DateTimeProperty(default=datetime.datetime.now)


class UserNode(StructuredNode):
    user_id = IntegerProperty()
    username = StringProperty()
