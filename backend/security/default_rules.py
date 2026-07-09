def get_rules():
    return [
        lambda e: "error" in str(e),
        lambda e: "inject" in str(e)
    ]