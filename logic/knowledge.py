class WorkingMemory:
    """
    stores all facts and reasoning during inference.
    """
    def __init__(self):
        self.facts = {}        # key -> value
        self.reasons = []      # list of strings
        self.output_text = None

    def assert_fact(self, key, value):
        self.facts[key] = value

    def get(self, key, default=None):
        return self.facts.get(key, default)

    def add_reason(self, reason):
        if reason not in self.reasons:
            self.reasons.append(reason)

    def set_output(self, text):
        self.output_text = text

