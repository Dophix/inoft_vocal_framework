from typing import List

from inoft_vocal_framework import Settings, InoftSkill
from inoft_vocal_framework.nodes.base_node import BaseNode
from inoft_vocal_framework.nodes.collection.audio_track import AudioTrackNode
from inoft_vocal_framework.nodes.collection.play_audio_file import PlayAudioFileNode, PlayerTimeModel
from inoft_vocal_framework.platforms_handlers.handler_input import HandlerInputWrapper, HandlerInput


class AudioBlockNode(BaseNode):
    def __init__(self, id: str, child: List[AudioTrackNode]):
        super().__init__(id_key=id, child=child)

    def serialize(self) -> dict:
        serialized_tracks: List[dict] = list()
        if self.child is not None:
            for track_item in self.child.values():
                serialized_tracks.append(track_item.serialize())
        return {'tracks': serialized_tracks}

    def __run__(self, context: HandlerInputWrapper):
        from inoft_vocal_framework.inoft_audio_engine_renderer.audio_engine_renderer_wrapping import render
        return render(audio_blocks=[self], out_filepath="F:/Sons utiles/tests/test_framework_1.mp3", out_format_type="mp3")


if __name__ == "__main__":
    audio_block = AudioBlockNode(
        id="d77d8c84-010c-44d3-ab47-ee6ca05f687e",
        child=[
            AudioTrackNode(id="4244273e-5d13-42b9-9c08-d0d3c9f8b1f6", child=[
                PlayAudioFileNode(
                    id="e79fcffb-d006-4f0e-bac6-6b17348a06b6",
                    file_url="example.com",
                    local_filepath="F:/Sons utiles/Pour Vous J'Avais Fait Cette Chanson - Jean Sablon.wav",
                    assigned_track_id="trackId1",
                    player_start_time=PlayerTimeModel(relationship_parent_id="parentId", type="parent_start-time", offset=0)
                ),
                PlayAudioFileNode(
                    id="e79fcffb-d006eaeaeaeaeaeea-4f0e-bac6-6b17348a06b6",
                    file_url="example.com",
                    local_filepath="F:/Sons utiles/ambiance_out.wav",
                    assigned_track_id="trackId1",
                    player_start_time=PlayerTimeModel(relationship_parent_id="parentId", type="parent_start-time", offset=10)
                ),
                # AudioSpeechNode(id="8052c916-d691-4976-854d-52bc34791210", text="Hello my dear friend", voice="Joanna")
            ])
        ]
    )
    skill = InoftSkill(settings_instance=Settings())
    audio_block.__run__(skill)
