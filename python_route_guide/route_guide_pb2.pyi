"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2015 gRPC authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
from builtins import (
    bool,
    int,
    str,
)
from google.protobuf.descriptor import (
    Descriptor,
    FileDescriptor,
)
from google.protobuf.message import (
    Message,
)

DESCRIPTOR: FileDescriptor

@typing_extensions.final
class Point(Message):
    """Points are represented as latitude-longitude pairs in the E7 representation
    (degrees multiplied by 10**7 and rounded to the nearest integer).
    Latitudes should be in the range +/- 90 degrees and longitude should be in
    the range +/- 180 degrees (inclusive).
    """

    DESCRIPTOR: Descriptor

    LATITUDE_FIELD_NUMBER: int
    LONGITUDE_FIELD_NUMBER: int
    latitude: int
    longitude: int
    def __init__(
        self,
        *,
        latitude: int = ...,
        longitude: int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["latitude", b"latitude", "longitude", b"longitude"]) -> None: ...

@typing_extensions.final
class Rectangle(Message):
    """A latitude-longitude rectangle, represented as two diagonally opposite
    points "lo" and "hi".
    """

    DESCRIPTOR: Descriptor

    LO_FIELD_NUMBER: int
    HI_FIELD_NUMBER: int
    @property
    def lo(self) -> Point:
        """One corner of the rectangle."""
    @property
    def hi(self) -> Point:
        """The other corner of the rectangle."""
    def __init__(
        self,
        *,
        lo: Point | None = ...,
        hi: Point | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hi", b"hi", "lo", b"lo"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hi", b"hi", "lo", b"lo"]) -> None: ...

@typing_extensions.final
class Feature(Message):
    """A feature names something at a given point.

    If a feature could not be named, the name is empty.
    """

    DESCRIPTOR: Descriptor

    NAME_FIELD_NUMBER: int
    LOCATION_FIELD_NUMBER: int
    name: str
    """The name of the feature."""
    @property
    def location(self) -> Point:
        """The point where the feature is detected."""
    def __init__(
        self,
        *,
        name: str = ...,
        location: Point | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["location", b"location"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "name", b"name"]) -> None: ...

@typing_extensions.final
class RouteNote(Message):
    """A RouteNote is a message sent while at a given point."""

    DESCRIPTOR: Descriptor

    LOCATION_FIELD_NUMBER: int
    MESSAGE_FIELD_NUMBER: int
    @property
    def location(self) -> Point:
        """The location from which the message is sent."""
    message: str
    """The message to be sent."""
    def __init__(
        self,
        *,
        location: Point | None = ...,
        message: str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["location", b"location"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["location", b"location", "message", b"message"]) -> None: ...

@typing_extensions.final
class RouteSummary(Message):
    """A RouteSummary is received in response to a RecordRoute rpc.

    It contains the number of individual points received, the number of
    detected features, and the total distance covered as the cumulative sum of
    the distance between each point.
    """

    DESCRIPTOR: Descriptor

    POINT_COUNT_FIELD_NUMBER: int
    FEATURE_COUNT_FIELD_NUMBER: int
    DISTANCE_FIELD_NUMBER: int
    ELAPSED_TIME_FIELD_NUMBER: int
    point_count: int
    """The number of points received."""
    feature_count: int
    """The number of known features passed while traversing the route."""
    distance: int
    """The distance covered in metres."""
    elapsed_time: int
    """The duration of the traversal in seconds."""
    def __init__(
        self,
        *,
        point_count: int = ...,
        feature_count: int = ...,
        distance: int = ...,
        elapsed_time: int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["distance", b"distance", "elapsed_time", b"elapsed_time", "feature_count", b"feature_count", "point_count", b"point_count"]) -> None: ...