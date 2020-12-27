from inoft_vocal_framework.nodes.base_node import BaseNode
from inoft_vocal_framework.platforms_handlers.handler_input import HandlerInputWrapper


class MultiplicationNode(BaseNode):
    def __init__(self, id: str, a: int or float, b: int or float):
        super().__init__(id_key=id)
        self.a = a
        self.b = b

    def __run__(self, context: HandlerInputWrapper):
        return self.a * self.b
