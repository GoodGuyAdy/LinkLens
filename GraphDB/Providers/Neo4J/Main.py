from neomodel import db, config
from neo4j.exceptions import ServiceUnavailable
from GraphDB.Providers.Base import BaseGraphDBProvider
from .Operations.Post.Entity import create_or_update_entity_node
from .Operations.Post.User import create_or_update_user_node
from .Operations.Post.Event import register_event_relation
from .Operations.Delete.Entity import delete_entity_node
from .Operations.Delete.User import delete_user_node
from .Operations.Get.Query import run_query
from LinkLens.settings import NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD


class Neo4JGraphDB(BaseGraphDBProvider):
    def __init__(self):
        try:
            neo4j_url = f"bolt://{NEO4J_USER}:{NEO4J_PASSWORD}@{NEO4J_URL}"
            config.DATABASE_URL = neo4j_url
            db.set_connection(neo4j_url)

        except ServiceUnavailable as e:
            print(f"Service unavailable: {e}")

    def sync_data(self):
        """Syncs all the data in primary storage in Graph DB"""
        pass

    def run_query(self, query):
        """Runs query in Graph DB and returns the data"""
        return run_query(query)

    def get_database_schema(self):
        """Returns the database schema"""
        pass

    def create_or_update_user(self, user_obj):
        """Creates or Updates a user node in Graph DB"""
        create_or_update_user_node(user_obj)

    def delete_user(self, user_obj):
        """Deletes a user node from Graph DB"""
        delete_user_node(user_obj)

    def create_or_update_entity(self, entity_obj):
        """Creates or Updates a entity node in Graph DB"""
        create_or_update_entity_node(entity_obj)

    def delete_entity(self, entity_obj):
        """Deletes a entity node in Graph DB"""
        delete_entity_node(entity_obj)

    def add_user_entity_relation(self, event_obj):
        """Adds a user to entity edge in Graph DB"""
        register_event_relation(event_obj)
