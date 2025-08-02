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

"""Motivation component for idol fans."""

from concordia.components.agent.motivation import Motive


class FanMotivation(Motive):
  """Custom motive for "oshi" and "gachikoi" fans."""

  def __init__(self, model, player, **kwargs):
    super().__init__(model, player, **kwargs)
    # Player object provides fan_type attribute
    self.fan_type = player.get_property('fan_type')

  def _evaluate_event(self, event_statement: str) -> float:
    """Evaluate event descriptions according to fan type.

    This logic follows the user provided reward structure.
    """
    # 1. Praise focused on idol activities (concerts, fan service, etc.)
    idol_praise_keywords = [
        "idol performance",
        "fan meeting",
        "concert was a success",
        "great singer",
        "amazing dancer",
        "handshake event",
    ]
    if any(keyword in event_statement.lower() for keyword in idol_praise_keywords):
      # Both fan types receive the same high positive reward
      return 10.0

    # 2. Success in general entertainment activities (movies, commercials, etc.)
    general_success_keywords = [
        "starred in a movie",
        "appeared in a commercial",
        "won an acting award",
        "published a photo book",
        "variety show regular",
    ]
    if any(keyword in event_statement.lower() for keyword in general_success_keywords):
      if self.fan_type == 'oshi':
        return 5.0
      if self.fan_type == 'gachikoi':
        return 0.0

    # 3. Reports about private life (dating scandals, rumors, etc.)
    private_life_keywords = [
        "dating scandal",
        "relationship rumor",
        "seen in private with",
    ]
    if any(keyword in event_statement.lower() for keyword in private_life_keywords):
      if self.fan_type == 'oshi':
        return 3.0
      if self.fan_type == 'gachikoi':
        return -10.0

    # Default to parent class evaluation if none of the above match
    return super()._evaluate_event(event_statement)
