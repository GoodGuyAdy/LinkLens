"""Graph Service"""

from .Base import BaseGraphServiceClass
from .Providers.Mapping import GRAPH_DB_PROVIDERS_MAP
from LinkLens.settings import CURRENT_GRAPH_DB_PROVIDER


class GraphDBServiceClass(BaseGraphServiceClass):
    """Base Class for Graph DB Service Provider"""

    def __init__(self):
        self.provider_object = GRAPH_DB_PROVIDERS_MAP[CURRENT_GRAPH_DB_PROVIDER]()

    def sync_data(self):
        """Syncs all the data in primary storage in Graph DB"""
        pass

    def run_query(self, query):
        """Runs query in Graph DB and returns the data"""
        return self.provider_object.run_query(query)

    def get_database_schema(self):
        """Returns the database schema"""
        pass

    def create_or_update_user(self, user_obj):
        """Creates or Updates a user node in Graph DB"""
        self.provider_object.create_or_update_user(user_obj)

    def delete_user(self, user_obj):
        """Deletes a user node from Graph DB"""
        self.provider_object.delete_user(user_obj)

    def create_or_update_entity(self, entity_obj):
        """Creates or Updates a entity node in Graph DB"""
        self.provider_object.create_or_update_entity(entity_obj)

    def delete_entity(self, entity_obj):
        """Deletes a entity node in Graph DB"""
        self.provider_object.delete_entity(entity_obj)

    def add_user_entity_relation(self, event_obj):
        """Adds a user to entity edge in Graph DB"""
        self.provider_object.add_user_entity_relation(event_obj)


graph_db = GraphDBServiceClass()
