
from graph_nodes import (
    router_node,
    name_node,
    age_node,
    query_node
)
from graph_state import PatientState



def run_graph(state):
    """
    Nodes ko ek order me run karta hai
    Aur pehla message return karta hai
    """

    # 1️⃣ Query node
    result = query_node(state)
    if result:
        return result

    # 2️⃣ Router node (ward decide)
    result = router_node(state)
    if result:
        state.update(result)

    # 3️⃣ Name node
    result = name_node(state)
    if result:
        return result

    # 4️⃣ Age node
    result = age_node(state)
    if result:
        return result

    # 5️⃣ Sab complete
    return {"message": "Thank you. Please proceed to the reception desk."}


