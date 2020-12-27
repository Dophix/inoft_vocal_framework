from abc import abstractmethod
from typing import Optional, List

from inoft_vocal_framework.platforms_handlers.handler_input import HandlerInputWrapper


class BaseNode:
    def __init__(self, id_key: str, child: Optional[list] = None):
        self._id = id_key
        self._child_dict = dict()
        if child is not None:
            for element in child:
                element: BaseNode
                self._child_dict[element.id] = element

    @property
    def id(self) -> str:
        return self._id

    @property
    def child(self) -> dict:
        return self._child_dict

    @abstractmethod
    def __run__(self, context: HandlerInputWrapper):
        raise Exception("__run__ function not implemented")

    def __serialize__(self) -> dict:
        raise Exception("__serialize__ function not implemented")

    def serialize(self) -> dict:
        serialized_data = self.__serialize__()
        serialized_data['id'] = self._id
        if self.child is not None:
            serialized_child: List[dict] = list()
            for child_item in self.child.values():
                child_element: BaseNode
                serialized_child.append(child_item.serialize())
            existing_serialized_child = serialized_data.get('child', [])
            serialized_child = [*serialized_child, *existing_serialized_child]
            if len(serialized_child) > 0:
                serialized_data['child'] = serialized_child
        return serialized_data
