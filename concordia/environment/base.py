# Copyright 2025 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple base environment."""

import datetime
from collections.abc import Sequence


class Environment:
  """Lightweight environment base class."""

  def __init__(self, scenario=None, *args, **kwargs):
    del args, kwargs
    self.scenario = scenario
    self._time = datetime.datetime.now()
    self._events: list[str] = []

  def tick(self) -> None:
    """Advance internal clock by one minute."""
    self._time += datetime.timedelta(minutes=1)

  def get_time(self) -> datetime.datetime:
    """Return the current simulation time."""
    return self._time

  def broadcast_event(self, event_statement: str) -> None:
    """Record a broadcast event.

    Subclasses may override this method to notify agents. Here we simply
    store the events in an internal list.
    """
    self._events.append(event_statement)

  def get_events(self) -> Sequence[str]:
    """Return the list of broadcast events."""
    return tuple(self._events)
