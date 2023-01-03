# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common resources used in the gRPC route guide example."""

import json

import route_guide_pb2


def read_route_guide_database():
    """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    import os
    script_dir = os.path.dirname(__file__)
    rel_path = 'route_guide_db.json'
    abs_file_path = os.path.join(script_dir, rel_path)
    
    feature_list = []
    with open(abs_file_path) as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = route_guide_pb2.Feature(
                name=item["name"],
                location=route_guide_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]))
            feature_list.append(feature)
    return feature_list