from scholarmind_core import ScholarMindCore


def test_core_initialization():
    core = ScholarMindCore()

    assert core is not None


def test_core_has_process_method():
    core = ScholarMindCore()

    assert hasattr(core, "process")


def test_core_process_returns_result():
    core = ScholarMindCore()

    result = core.process("AI research")

    assert result is not None 