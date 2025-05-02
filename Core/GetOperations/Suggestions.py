from GraphDB.GraphService import graph_db
from LLM.Response.Main import generate_ai_response


def get_ai_suggestion(username, entity_type):
    """
    Generates AI response on graph data an suggests user more entities like the entity_type provided
    """

    llm_suggestion_query = """
        You will be provided with graph data containing nodes and edges. The nodes are of two types:
        UserNode: Properties - user_id, username.
        EntityNode: Properties - entity_name, entity_type.
        Based on the filtered data for a specific username and entity_type that I will provide in the context, analyze the graph and suggest 5 entities the user is likely to be interested in.
        For each entity, give a brief explanation of why it might be relevant, considering their connections in the graph (both direct and indirect).
        Do not mention 'graph data' or 'given graph data' anywhere in the response you provide. Act like you are talking to the user.
    """

    graph_db_query = f"""
        MATCH (user:UserNode {{username: '{username}'}})-[edge]->(entity:EntityNode {{entity_type: '{entity_type}'}})
        RETURN user, edge, entity
    """

    context = graph_db.run_query(graph_db_query)

    response = generate_ai_response(llm_suggestion_query, context)

    return response
