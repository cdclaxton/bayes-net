from BN import *


def run_query(edges, queries):
    """Run a query on a graph."""

    # Preconditions
    assert isinstance(edges, list), f"Expected a list, got {type(edges)}"
    assert isinstance(queries, list), f"Expected a list, got {type(queries)}"

    # Build the graph
    net = BN()
    for edge in edges:
        assert isinstance(edge, str), f"Expected a str, got {type(edge)}"
        assert " " in edge, f"Expected two nodes separated by a space"
        nodes = edge.split(" ")
        assert len(nodes) == 2, f"Expected two nodes, found {len(nodes)}"
        net.add_edge(nodes)

    # Run the queries
    for (start, end, observed) in queries:
        assert isinstance(start, str), f"Expected a str, got {type(start)}"
        assert isinstance(end, str), f"Expected a str, got {type(end)}"
        assert isinstance(
            observed, list), f"Expected a str, got {type(observed)}"

        d_sep = net.is_dsep(start, end, observed)

        if len(observed) == 0:
            print(f"Are {start} and {end} d-separated? {d_sep}")
        else:
            obs = "{" + ",".join(observed) + "}"
            print(f"Are {start} and {end} d-separated given {obs}? {d_sep}")


if __name__ == '__main__':

    run_query(
        edges=["A B", "B C"],
        queries=[("A", "C", []),
                 ("A", "C", ["B"])])

    print("---")

    run_query(
        edges=["CA E", "C E"],
        queries=[("CA", "C", []),
                 ("CA", "C", ["E"])]
    )

    print("---")

    run_query(
        edges=["C W", "C E"],
        queries=[("W", "E", ["C"])]
    )
