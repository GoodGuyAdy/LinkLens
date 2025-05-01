from Models.Event import Event
from Models.User import User
from Models.Entity import Entity
from django.dispatch import receiver
from GraphDB.GraphService import graph_db
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=Entity)
def graph_db_save_entity(sender, instance, created, **kwargs):
    """Saves an entity in Graph DB"""
    graph_db.create_or_update_entity(instance)


@receiver(post_delete, sender=Entity)
def graph_db_delete_entity(sender, instance, **kwargs):
    """Deletes an entity from Graph DB"""
    graph_db.delete_entity(instance)


@receiver(post_save, sender=User)
def graph_db_save_user(sender, instance, created, **kwargs):
    """Saves a user in Graph DB"""
    graph_db.create_or_update_user(instance)


@receiver(post_delete, sender=User)
def graph_db_delete_user(sender, instance, **kwargs):
    """Deletes a user from Graph DB"""
    graph_db.delete_user(instance)


@receiver(post_save, sender=Event)
def graph_db_save_event(sender, instance, created, **kwargs):
    """Saves an event in Graph DB"""
    graph_db.add_user_entity_relation(instance)
