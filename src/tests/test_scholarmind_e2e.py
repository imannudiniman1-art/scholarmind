from scholarmind_core import ScholarMind


def test_scholarmind_end_to_end():
    system = ScholarMind("data")

    assert system is not None

    assert hasattr(system, "load_data")
    assert hasattr(system, "search")
    assert hasattr(system, "answer")
    assert hasattr(system, "ask_about_paper")
    assert hasattr(system, "status")

    status = system.status()

    assert isinstance(status, dict)
    assert "papers" in status
    assert "memory_items" in status
    assert "graph_nodes" in status
    assert "graph_relationships" in status