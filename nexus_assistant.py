
from base_plugin import BasePlugin, MenuItemData, MenuItemType
from client_utils import get_last_fragment
from ui.alert import AlertDialogBuilder

from android.graphics import Color
from android.view import Gravity
from android.widget import LinearLayout, TextView, EditText, Button
from org.telegram.messenger import AndroidUtilities


__id__ = "nexus_assistant"
__name__ = "Nexus Assistant"
__description__ = "Personal assistant for exteraGram"
__author__ = "Nexus"
__version__ = "1.0.0"
__icon__ = "exteraPlugins/1"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.4.3"
__category__ = ["tools", "integrations"]


class NexusAssistant(BasePlugin):

    def on_plugin_load(self):
        self.menu_item_id = self.add_menu_item(
            MenuItemData(
                menu_type=MenuItemType.DRAWER_MENU,
                text="NEXUS",
                icon="msg_info",
                subtext="Personal Assistant",
                on_click=self.open_nexus,
                priority=100
            )
        )

        self.logger.info("NEXUS loaded")

    def on_plugin_unload(self):
        self.logger.info("NEXUS unloaded")

    def open_nexus(self, context):
        fragment = get_last_fragment()

        if not fragment:
            self.logger.warning("No active fragment")
            return

        activity = fragment.getParentActivity()

        if not activity:
            self.logger.warning("No active activity")
            return

        self.show_interface(activity)

    def show_interface(self, activity):

        dp = AndroidUtilities.dp

        root = LinearLayout(activity)
        root.setOrientation(LinearLayout.VERTICAL)
        root.setGravity(Gravity.CENTER_HORIZONTAL)
        root.setPadding(dp(20), dp(18), dp(20), dp(18))
        root.setBackgroundColor(Color.rgb(12, 12, 12))

        # Logo
        logo = TextView(activity)
        logo.setText("N E X U S")
        logo.setTextSize(25)
        logo.setTextColor(Color.WHITE)
        logo.setGravity(Gravity.CENTER)
        root.addView(
            logo,
            LinearLayout.LayoutParams(-1, dp(55))
        )

        # Mascot placeholder
        mascot = TextView(activity)
        mascot.setText("◜       ◝\n\n   ◉   ◉\n\n      ᴗ")
        mascot.setTextSize(27)
        mascot.setTextColor(Color.WHITE)
        mascot.setGravity(Gravity.CENTER)

        root.addView(
            mascot,
            LinearLayout.LayoutParams(-1, dp(145))
        )

        # Greeting
        greeting = TextView(activity)
        greeting.setText("Привет! Я NEXUS.")
        greeting.setTextSize(21)
        greeting.setTextColor(Color.WHITE)
        greeting.setGravity(Gravity.CENTER)

        root.addView(
            greeting,
            LinearLayout.LayoutParams(-1, dp(45))
        )

        description = TextView(activity)
        description.setText(
            "Твой личный помощник.\n"
            "Я готовлюсь к нашей первой беседе."
        )
        description.setTextSize(14)
        description.setTextColor(Color.LTGRAY)
        description.setGravity(Gravity.CENTER)

        root.addView(
            description,
            LinearLayout.LayoutParams(-1, dp(55))
        )

        # Message field
        input_field = EditText(activity)
        input_field.setHint("Напиши сообщение...")
        input_field.setTextColor(Color.WHITE)
        input_field.setHintTextColor(Color.GRAY)
        input_field.setTextSize(15)
        input_field.setSingleLine(False)
        input_field.setBackgroundColor(Color.rgb(32, 32, 32))
        input_field.setPadding(
            dp(14), dp(12), dp(14), dp(12)
        )

        root.addView(
            input_field,
            LinearLayout.LayoutParams(-1, dp(55))
        )

        # Voice button
        voice_button = Button(activity)
        voice_button.setText("ГОЛОСОВОЙ РЕЖИМ — СКОРО")
        voice_button.setEnabled(False)

        root.addView(
            voice_button,
            LinearLayout.LayoutParams(-1, dp(48))
        )

        # Send button
        send_button = Button(activity)
        send_button.setText("ОТПРАВИТЬ — СКОРО")
        send_button.setEnabled(False)

        root.addView(
            send_button,
            LinearLayout.LayoutParams(-1, dp(48))
        )

        builder = AlertDialogBuilder(activity)
        builder.set_title("NEXUS ASSISTANT")
        builder.set_view(root)
        builder.set_negative_button(
            "Закрыть",
            lambda dialog, which: dialog.dismiss()
        )
        builder.show()
        
