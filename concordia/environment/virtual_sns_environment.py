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

"""Environment that randomly emits idol related events."""

import random
import pandas as pd  # pylint: disable=unused-import

from concordia.environment.base import Environment


class VirtualSnsEnvironment(Environment):
  """A virtual SNS environment emitting entertainment news."""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Attempt to derive idol name from scenario configuration; fallback to literal
    try:
      self.idol_name = self.scenario.get_player_by_name('Idol').name
    except Exception:  # pylint: disable=broad-except
      self.idol_name = 'Idol'

    self._possible_events = [
        # Praise of idol specific activities
        f"{self.idol_name}'s idol performance at the concert was a success.",
        f"{self.idol_name}'s fan meeting was highly praised by attendees.",
        f"Fans are excited about {self.idol_name}'s amazing dancing in the new music video.",
        # Success in broader entertainment activities
        f"{self.idol_name} has been cast to star in a new movie.",
        f"{self.idol_name} will appear in a new nationwide commercial.",
        f"{self.idol_name} won a prestigious acting award.",
        # Private life reports
        f"A dating scandal involving {self.idol_name} was reported by a magazine.",
        f"There is a relationship rumor about {self.idol_name}.",
        # Other general events
        f"{self.idol_name} announced a new single release.",
        f"A documentary about {self.idol_name}'s journey will be aired.",
    ]

  def tick(self):
    super().tick()
    current_time = self.get_time()
    # Trigger a random event at 18:00 each day with 25% probability
    if current_time.hour == 18 and current_time.minute == 0 and random.random() < 0.25:
      event_statement = random.choice(self._possible_events)
      # Broadcast the event so all agents may observe it
      self.broadcast_event(event_statement)
