
def Override(interface):
    def check(method):
        assert method.__name__ in dir(interface), f"Warning: Method " \
                                                  f" {interface.__name__}.{method.__name__} " \
                                                  f"is not being overriden!"
        return method
    return check
