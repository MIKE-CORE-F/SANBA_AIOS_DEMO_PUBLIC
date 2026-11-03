"""
AI-OS FUSION - KERNEL TASK SCHEDULER (demo stub)
Records tasks in a list. It does not distribute them over threads.
"""


class Task:
    pass


class TaskScheduler:
    def __init__(self, max_threads=32):
        self.max_threads = max_threads
        self.tasks = []
        print(f"[TASK SCHEDULER] Demo stub: {self.max_threads} threads configured (no worker threads started).")

    def schedule_task(self, task_name: str, priority: int = 1, required_threads: int = 4) -> bool:
        self.tasks.append({"name": task_name, "priority": priority, "required_threads": required_threads})
        print(f"[TASK SCHEDULER] Task '{task_name}' recorded (demo stub, not executed).")
        return True
