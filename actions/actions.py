# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher, Action
import webbrowser
from rasa_sdk.interfaces import Action
from rasa_sdk.events import SlotSet ,EventType
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher , Action
from rasa_sdk.types import DomainDict


class ActionTellName(Action):

    def name(self) -> Text:
        return "action_tell_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        message = " Hi {}! , what is your mobile number ? ".format(name)
        print (message)
        dispatcher.utter_message(text=message)
        return []

class ActionTellName(Action):

    def name(self) -> Text:
        return "action_tell_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        number = tracker.get_slot("number")
      #  - text : " Hi {name}! , what is your mobile number 📱 ? "
        message = " Yeah , Your mobile number   is {} . Thanks for giving information ".format(number)
        print (message)
        dispatcher.utter_message(text=message)
        return []


class ValidateHealthForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_health_form"

  async def required_slots(
    self,
    slots_mapped_in_domain: List[Text],
    dispatcher: "CollectingDispatcher",
    tracker: "Tracker",
    domain: "DomainDict"
  ) -> List[Text]:
    if tracker.get_slot("confirm_exercise") == True:
      return ["confirm_exercise", "exercise", "sleep", "diet", "stress", "goal"]
    else:
      return ["confirm_exercise", "sleep", "diet", "stress", "goal"]

