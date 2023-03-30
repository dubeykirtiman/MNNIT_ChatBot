# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from mysql_connectivity import insertquery
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
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
        message = " Your mobile number is {} ".format(number)
        print (message)
        dispatcher.utter_message(text=message)
        return []
    
class ActionVideo(Action):
    def name(self) -> Text:
        return "action_query"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("storing details for future evaluation.")
        insertquery(tracker.get_slot("query"),tracker.get_slot("username"),tracker.get_slot("usermail"))

        return []

        
