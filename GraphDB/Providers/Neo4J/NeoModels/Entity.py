from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty
)


class EntityNode(StructuredNode):
    entity_id = IntegerProperty()
    entity_name = StringProperty()
    entity_type = StringProperty()
