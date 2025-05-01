from abc import ABC, abstractmethod


class BaseGraphServiceClass(ABC):
    """Base Class for Graph DB Service"""

    @abstractmethod
    def sync_data(self):
        """Syncs all the data in primary storage in Graph DB"""
        pass

    @abstractmethod
    def run_query(self):
        """Runs query in Graph DB and returns the data"""
        pass

    @abstractmethod
    def get_database_schema(self):
        """Returns the database schema"""
        pass

    @abstractmethod
    def create_or_update_user(self):
        """Creates or Updates a user node in Graph DB"""
        pass

    @abstractmethod
    def delete_user(self):
        """Deletes a user node from Graph DB"""
        pass

    @abstractmethod
    def create_or_update_entity(self):
        """Creates or Updates a entity node in Graph DB"""
        pass

    @abstractmethod
    def delete_entity(self):
        """Deletes a entity node in Graph DB"""
        pass

    @abstractmethod
    def add_user_entity_relation(self):
        """Adds a user to entity edge in Graph DB"""
        pass
