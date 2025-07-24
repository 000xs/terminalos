def test_import():
    import terminalos
    assert hasattr(terminalos, "__version__")   # or any other public symbol