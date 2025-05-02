from GraphDB.GraphService import graph_db
from LLM.Response.Main import generate_ai_response


def chat_to_data(llm_query):
    """
    Generates AI response on graph data based on the query user provides
    """

    context = graph_db.run_query(query=None)

    response = generate_ai_response(llm_query, context)

    return response
