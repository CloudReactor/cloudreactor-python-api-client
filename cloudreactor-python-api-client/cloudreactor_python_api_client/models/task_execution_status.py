from enum import Enum


class TaskExecutionStatus(str, Enum):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    TERMINATED_AFTER_TIME_OUT = "TERMINATED_AFTER_TIME_OUT"
    MARKED_DONE = "MARKED_DONE"
    EXITED_AFTER_MARKED_DONE = "EXITED_AFTER_MARKED_DONE"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ABANDONED = "ABANDONED"
    MANUALLY_STARTED = "MANUALLY_STARTED"
    ABORTED = "ABORTED"

    def __str__(self) -> str:
        return str(self.value)
