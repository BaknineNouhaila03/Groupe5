class Task:
    def __init__(self, task_id: str, description: str, state: str):
        self.id: str = task_id
        self.description: str = description
        self.state :str = state
