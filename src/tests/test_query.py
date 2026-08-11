from query import query


def test_query_returns_result():
    result = query("AI research")

    assert result is not None