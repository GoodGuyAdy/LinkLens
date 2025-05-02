from neomodel import db
from ...Response.Response import transform_to_json


def run_query(query):
    """Runs a query in neo4j and returns json data"""
    if not query:
        query = """
            MATCH (n)-[r]->(m)
            RETURN n, r, m
        """

    result = db.cypher_query(query)
    result_json = transform_to_json(result)
    return result_json
