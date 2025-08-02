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

"""Base classes for motives used by agents."""

from concordia.typing import entity_component


class Motive(entity_component.ComponentWithLogging):
  """Base motive component.

  Subclasses should override `_evaluate_event` to return a numeric reward
  for a given event description.
  """

  def __init__(self, model, player, **kwargs):
    del kwargs
    super().__init__()
    self._model = model
    self._player = player

  def get_state(self) -> entity_component.ComponentState:
    """Returns the (stateless) component state."""
    return {}

  def set_state(self, state: entity_component.ComponentState) -> None:
    """Restores the component state (no-op)."""
    del state
    return None

  def evaluate_event(self, event_statement: str) -> float:
    """Evaluate an event statement and return a reward."""
    reward = self._evaluate_event(event_statement)
    self._logging_channel({'Key': 'Reward', 'Value': reward})
    return reward

  def _evaluate_event(self, event_statement: str) -> float:
    """Default evaluation returning neutral reward.

    Subclasses should override this method.
    """
    del event_statement
    return 0.0
