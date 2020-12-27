from dataclasses import dataclass
from typing import List, Optional
from inoft_vocal_framework.nodes.base_node import BaseNode
from inoft_vocal_framework.platforms_handlers.handler_input import HandlerInputWrapper


@dataclass
class PlayerTimeModel:
    relationship_parent_id: str
    type: str
    offset: Optional[int or float]


class PlayAudioFileNode(BaseNode):
    def __init__(self, id: str, file_url: str, local_filepath: str, assigned_track_id: str, player_start_time: PlayerTimeModel, gain: Optional[int or float] = 1,
                 file_start_time: Optional[int or float] = None, file_end_time: Optional[int or float] = None):
        super().__init__(id_key=id)
        self.file_url = file_url
        self.local_filepath = local_filepath
        self.assigned_track_id = assigned_track_id
        self.player_start_time = player_start_time
        self.gain = gain
        self.file_start_time = file_start_time
        self.file_end_time = file_end_time

    def __serialize__(self) -> dict:
        return {
            'file_url': self.file_url,
            'local_filepath': self.local_filepath,
            'assigned_track_id': self.assigned_track_id,
            'player_start_time': self.player_start_time.__dict__,
            'player_end_time': {'type': 'until-self-end', 'relationship_parent_id': '', 'offset': 0},  # todo: remove player_end_time
            'gain': self.gain,
            'file_start_time': self.file_start_time,
            'file_end_time': self.file_end_time
        }

    def __run__(self, context: HandlerInputWrapper):
        pass
