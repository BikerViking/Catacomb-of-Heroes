from abc import abstractmethod

class State(object):  # metaclass=ABCMeta # Maybe...
    """docstring for State."""
    def __init__(self):
        super(State, self).__init__()

        self.__is_running = True
        self.__is_paused = False

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def pause():
        pass

    @abstractmethod
    def resume():
        pass

    @abstractmethod
    def close():
        pass

    @abstractmethod
    def switch_is_running():
        pass

    def get_is_running():
        return self.__is_running

    @abstractmethod
    def switch_is_paused():
        pass

    def get_is_paused():
        return self.__is_paused

    @abstractmethod
    def get_next_state():
        pass

    @abstractmethod
    def recieve_arg():
        pass

    @abstractmethod
    def pass_arg():
        pass
