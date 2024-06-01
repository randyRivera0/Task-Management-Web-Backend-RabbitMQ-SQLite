import json

# FIXME: automatically create task_id


class Task:
    id = 0
    def __init__(self, name, description, deadline, importance, duration, id=0, progress=0, state=0, blocked=False, blocked_by=None, block_reason=None, creation_time=None):
        self.id = Task.generate_id()
        self.name = name
        self.description = description

        self.deadline = deadline
        self.importance = importance # enum: HIGH, MEDIUM, LOW
        self.duration = duration
        self.progress = progress

        self.state = state
        self.blocked = blocked
        self.blocked_by = blocked_by
        self.block_reason = block_reason
        self.creation_time = creation_time
    

    @staticmethod
    def generate_id():
        Task.id += 1
        return Task.id


    def to_json(self):
        return json.dumps(self.__dict__)
