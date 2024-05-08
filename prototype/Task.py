import json

# TODO: Define Task properties

class Task:
    def __init__(self, id, name, importance, urgency, time, description, state, progress, blocked=False, block_reason=None):
        self.id = id
        self.name = name
        self.importance = importance
        self.urgency = urgency
        self.time = time
        self.description = description
        self.state = state
        self.progress = progress
        self.blocked = blocked
        self.block_reason = block_reason


    def to_json(self):
        return json.dumps(self.__dict__)
