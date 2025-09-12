from datetime import datetime, timedelta


class Task:
    def __init__(self, task_id: str, description: str, state: str,
                 started_at: datetime, interval: timedelta ):
        self.id: str = task_id
        self.description: str = description
        self.state :str = state
        self.started_at = started_at
        self.interval = interval
