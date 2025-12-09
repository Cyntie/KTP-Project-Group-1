class Rule:
    """
    Simple forward-chaining rule: IF condition(wm) THEN action(wm)
    """
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition  # WorkingMemory -> bool
        self.action = action        # WorkingMemory -> None

    def try_fire(self, wm):
        if self.condition(wm):
            self.action(wm)
            return True
        return False


