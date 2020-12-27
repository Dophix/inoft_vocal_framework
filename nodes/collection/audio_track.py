from typing import List, Optional
from inoft_vocal_framework.nodes.base_node import BaseNode
from inoft_vocal_framework.nodes.collection.play_audio_file import PlayAudioFileNode
from inoft_vocal_framework.platforms_handlers.handler_input import HandlerInputWrapper


class AudioTrackNode(BaseNode):
    def __init__(self, id: str, gain: Optional[float or int] = 1, child: Optional[List[PlayAudioFileNode]] = None):
        super().__init__(id_key=id, child=child)
        self.gain = gain

    def __serialize__(self) -> dict:
        return {
            'gain': self.gain
        }

    def __run__(self, context: HandlerInputWrapper):
        pass
