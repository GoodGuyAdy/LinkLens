import json
import neo4j


def safe_json_parse(data):
    if isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return {}
    return data


def node_to_dict(node):
    node_type = list(node.labels)[0]
    properties = dict(node._properties)

    return {
        "id": node.element_id,
        "type": node_type,
        "properties": properties,
    }


def relationship_to_dict(relationship):
    return {
        "id": relationship.element_id,
        "source": relationship.start_node.element_id,
        "target": relationship.end_node.element_id,
        "type": relationship.type,
    }


def transform_to_json(data):
    """
    Transforms Neo4j query result into a json with nodes and edges.
    """

    nodes = []
    edges = []
    seen_nodes = set()
    seen_edges = set()

    def add_node(node):
        node_id = node.element_id
        if node_id not in seen_nodes:
            nodes.append(node_to_dict(node))
            seen_nodes.add(node_id)

    def add_edge(edge):
        edge_id = edge.element_id
        if edge_id not in seen_edges:
            edges.append(relationship_to_dict(edge))
            seen_edges.add(edge_id)

    def process_item(item):
        if isinstance(item, neo4j.graph.Node):
            add_node(item)
        elif isinstance(item, neo4j.graph.Relationship):
            add_edge(item)
        elif isinstance(item, list):
            for sub_item in item:
                process_item(sub_item)

    if not data or not data[0]:
        return {"Nodes": [], "Edges": []}

    for record in data[0]:
        process_item(record)

    return {"Nodes": nodes, "Edges": edges}
