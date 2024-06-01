import json

# FIXME: automatically create task_id


class Task:
    def __init__(self, name, description, state, importance):
        self.name = name
        self.description = description
        self.state = state
        self.importance = importance # enum: HIGH, MEDIUM, LOW

        
    def to_json(self):
        return json.dumps(self.__dict__)
