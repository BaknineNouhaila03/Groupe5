class Task:
    def __init__(self, task_id: str, description: str, etat: str):
        self.id: str = task_id
        self.description: str = description
        self.etat :str = etat
