from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MusicSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MUSIC_SOURCE_UNSPECIFIED: _ClassVar[MusicSource]
    MUSIC_SOURCE_BACKGROUND: _ClassVar[MusicSource]
    MUSIC_SOURCE_SYSTEM_AUDIO: _ClassVar[MusicSource]

class InferenceRoute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFERENCE_ROUTE_UNSPECIFIED: _ClassVar[InferenceRoute]
    INFERENCE_ROUTE_MAPPER: _ClassVar[InferenceRoute]
    INFERENCE_ROUTE_TIMING_MOCK: _ClassVar[InferenceRoute]

class EndpointStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENDPOINT_STATUS_UNSPECIFIED: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_READY: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_AUDIO_PREPARING: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_AUDIO_READY: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_STREAMING: _ClassVar[EndpointStatus]
    ENDPOINT_STATUS_STOPPED: _ClassVar[EndpointStatus]
MUSIC_SOURCE_UNSPECIFIED: MusicSource
MUSIC_SOURCE_BACKGROUND: MusicSource
MUSIC_SOURCE_SYSTEM_AUDIO: MusicSource
INFERENCE_ROUTE_UNSPECIFIED: InferenceRoute
INFERENCE_ROUTE_MAPPER: InferenceRoute
INFERENCE_ROUTE_TIMING_MOCK: InferenceRoute
ENDPOINT_STATUS_UNSPECIFIED: EndpointStatus
ENDPOINT_STATUS_READY: EndpointStatus
ENDPOINT_STATUS_AUDIO_PREPARING: EndpointStatus
ENDPOINT_STATUS_AUDIO_READY: EndpointStatus
ENDPOINT_STATUS_STREAMING: EndpointStatus
ENDPOINT_STATUS_STOPPED: EndpointStatus

class Envelope(_message.Message):
    __slots__ = ("session_id", "sequence", "sent_at_unix_ms", "ready", "audio", "reference_time", "stop_session", "hit_object_token", "error", "status")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_SESSION_FIELD_NUMBER: _ClassVar[int]
    HIT_OBJECT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    sequence: int
    sent_at_unix_ms: int
    ready: ReadyRequest
    audio: AudioRequest
    reference_time: ReferenceTimeRequest
    stop_session: StopSessionRequest
    hit_object_token: HitObjectTokenEvent
    error: ErrorEvent
    status: StatusEvent
    def __init__(self, session_id: _Optional[str] = ..., sequence: _Optional[int] = ..., sent_at_unix_ms: _Optional[int] = ..., ready: _Optional[_Union[ReadyRequest, _Mapping]] = ..., audio: _Optional[_Union[AudioRequest, _Mapping]] = ..., reference_time: _Optional[_Union[ReferenceTimeRequest, _Mapping]] = ..., stop_session: _Optional[_Union[StopSessionRequest, _Mapping]] = ..., hit_object_token: _Optional[_Union[HitObjectTokenEvent, _Mapping]] = ..., error: _Optional[_Union[ErrorEvent, _Mapping]] = ..., status: _Optional[_Union[StatusEvent, _Mapping]] = ...) -> None: ...

class ReadyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AudioRequest(_message.Message):
    __slots__ = ("audio_path", "audio_length_ms", "music_source", "difficulty", "route")
    AUDIO_PATH_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    MUSIC_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    audio_path: str
    audio_length_ms: int
    music_source: MusicSource
    difficulty: float
    route: InferenceRoute
    def __init__(self, audio_path: _Optional[str] = ..., audio_length_ms: _Optional[int] = ..., music_source: _Optional[_Union[MusicSource, str]] = ..., difficulty: _Optional[float] = ..., route: _Optional[_Union[InferenceRoute, str]] = ...) -> None: ...

class ReferenceTimeRequest(_message.Message):
    __slots__ = ("ref_time_ms", "local_host_time_send_ms", "audio_length_ms")
    REF_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_HOST_TIME_SEND_MS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    ref_time_ms: int
    local_host_time_send_ms: float
    audio_length_ms: int
    def __init__(self, ref_time_ms: _Optional[int] = ..., local_host_time_send_ms: _Optional[float] = ..., audio_length_ms: _Optional[int] = ...) -> None: ...

class StopSessionRequest(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class HitObjectTokenEvent(_message.Message):
    __slots__ = ("token_id", "ms_in_ref_audio")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    MS_IN_REF_AUDIO_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    ms_in_ref_audio: int
    def __init__(self, token_id: _Optional[int] = ..., ms_in_ref_audio: _Optional[int] = ...) -> None: ...

class ErrorEvent(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class StatusEvent(_message.Message):
    __slots__ = ("status", "message", "ref_time_ms", "local_host_time_ms")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REF_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_HOST_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    status: EndpointStatus
    message: str
    ref_time_ms: int
    local_host_time_ms: float
    def __init__(self, status: _Optional[_Union[EndpointStatus, str]] = ..., message: _Optional[str] = ..., ref_time_ms: _Optional[int] = ..., local_host_time_ms: _Optional[float] = ...) -> None: ...
