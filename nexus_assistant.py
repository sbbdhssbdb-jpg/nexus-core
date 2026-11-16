
from typing import Any, List

from base_plugin import BasePlugin
from ui.settings import Header, Switch, Text

__id__ = "nexus_assistant"
__name__ = "Nexus Assistant"
__description__ = "Personal assistant for exteraGram"
__author__ = "Nexus"
__version__ = "1.0.0"
__icon__ = "exteraPlugins/1"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.4.3"
__category__ = ["tools"]

class NexusAssistant(BasePlugin):

    def create_settings(self) -> List[Any]:
        return [
            Header(text="NEXUS ASSISTANT"),
            Text(
                text="Nexus",
                subtext="Your personal assistant"
            ),
            Header(text="General settings"),
            Switch(
                key="assistant_enabled",
                text="Enable Nexus",
                default=True
            ),
            Switch(
                key="notifications",
                text="Notifications",
                default=True
            ),
            Header(text="Information"),
            Text(
                text="Version 1.0.0",
                subtext="Nexus Assistant for exteraGram"
            )
        ]
        
