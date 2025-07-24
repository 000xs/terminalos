def test_import():
    import terminalos
    assert hasattr(terminalos, "__version__")   # or any other public symbol
    
# test dependacey
def test_core_packages():
    import terminalos
    assert hasattr(terminalos, "core")

    
def test_config_packages():
    import terminalos
    assert hasattr(terminalos, "config")

    

    