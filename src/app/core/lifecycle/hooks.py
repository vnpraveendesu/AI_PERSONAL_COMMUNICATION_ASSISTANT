from abc import ABC, abstractmethod


class LifecycleHook(ABC):
    """
    Interface for startup/shutdown components.
    """

    @abstractmethod
    def startup(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
