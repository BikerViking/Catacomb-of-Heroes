from ../model import model

class MainController(object):
    """docstring for MainController."""
    def __init__(self, surface, input):
        super(MainController, self).__init__()

        self.__surface = surface # window.core_surface
        self.__input = input # input.event_handler
        #self.__sound = sound # no idea how

        self.__load_model = model.load_model.LoadModel()
