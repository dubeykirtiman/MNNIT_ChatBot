# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher, Action
import webbrowser
from rasa_sdk.interfaces import Action
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher 

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(self, dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        video_url="https://youtu.be/j76Z57O0Acw"
        dispatcher.utter_message(text="wait... Playing your video.")
        webbrowser.open(video_url)
        return []
# class ValidateRestaurantForm(Action):
  #  def name(self) -> Text:
  #     return "user_details_form"

   # def run(
      #   self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text -> Any]) -> List[EventType]:
   #     required_slots = ["name", "number"]

    #    for slot_name in required_slots:
         #   if tracker.slots.get(slot_name) is None:
         #       "The slot is not filled yet. Request the user to fill this slot next."
          #     return [SlotSet("requested_slot", slot_name)]

               
      #  return [SlotSet("requested_slot", None)] 
      #return []

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks", Name=tracker.get_slot("name"),Mobile_number=tracker.get_slot("number"))
        
        
class ActionImage(Action):
    def name(self) -> Text:
        return 'action_image'

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: Dict) -> List[Dict[Text, Any]]:
        image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shiksha.com%2Funiversity%2Fmnnit-allahabad-motilal-nehru-national-institute-of-technology-24357&psig=AOvVaw2Huxtg15KnizdKpPlfMjVG&ust=1679021555456000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCICx0ea43_0CFQAAAAAdAAAAABAE"
        dispatcher.utter_message(text="Please.... wait image is upload..")
        webbrowser.open(image_url)
        return []
    
class ActionGreet(Action):
    def name(self) -> Text:
        return 'action_greet'
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message(text="MNNIT is the great campus")
        return []
    
# class ValidateRegisterForm(FormValidationAction):
#     def name(self) -> Text:
#         return 'validate_register_form'
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         return []

#     def validate_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate slot value."""
#         if not slot_value:
#          return {"utter_ask_registeremail": None}
#         else: 
#          return {"utter_ask_registeremail": slot_value}	
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitregister"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        user_name = tracker.get_slot("registeremail")
        print("email id  is  : ",user_name) 
        
		
        dispatcher.utter_message(template="utter_details_thanks")
        return []
    
# class ActionDefaultFallback(Action):
#     # Executes the fallback action and goes back to the previous state
#     # of the dialogue

#     def name(self) -> Text:
#         return ACTION_DEFAULT_FALLBACK_NAME

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="my_custom_fallback_template")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]
 
# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         # tell the user they are being passed to a customer service agent
#         dispatcher.utter_message(text="I am passing you to a human...")
     

#         return [ UserUtteranceReverted()]
