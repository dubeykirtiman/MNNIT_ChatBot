# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from mysql_connectivity import DataUpdate
import spacy
import openai
from dotenv import load_dotenv
load_dotenv()
import os

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
        print(message)
        dispatcher.utter_message(text=message)
        return []
    
# class ActionSubmit(Action):

#     def name(self) -> Text:
#         return "action_submit"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         name = tracker.get_slot("name")
#         # usermail = tracker.get_slot("usermail")
#         question = tracker.get_slot("question")
#         DataUpdate(name,question)
#         return[]

# class IntroduceAction(Action):
#     def name(self) -> Text:
#         return "action_introduce"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         name_entity = tracker.latest_message.get("entities", {}).get("name", None)
#         if name_entity:
#             name = name_entity[0].get("value")
#             # Do something with the extracted name entity
#             dispatcher.utter_message(text=f"Nice to meet you, {name}!")
#         else:
#             dispatcher.utter_message(text="Sorry, I didn't catch your name.")
#         return []

class ExtractNamesAction(Action):
    def name(self):
        return "action_introduce"
    
    def run(self, dispatcher, tracker, domain):
        # Load Spacy NLP model
        nlp = spacy.load("en_core_web_md")

        # Extract names from user input
        user_input = tracker.latest_message.get("text")
        doc = nlp(user_input)
        print(user_input)
        # print(doc)
        # names = []
        names=[]
        for ent in doc.ents:
            if ent.label_== "PERSON":
                names.append(ent.text)
        # Set extracted names as a slot
        print(names)
        if(names==[]):
            names=user_input
        print("action1")
        # dispatcher.utter_message(text=f"Nice to meet you, {names}!")
        return [SlotSet("name",names)]
    
# class ExtractNamesAction2(Action):
#     def name(self):
#         return "action_introduce2"

#     # def run(self, dispatcher, tracker, domain):
#         # Load Spacy NLP model
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         nlp = spacy.load("en_core_web_md")
#         # Extract names from user input
#         user_input = tracker.latest_message.get("text")
#         doc = nlp(user_input)
#         print(user_input)
#         questionquery = tracker.get_slot("question")
#         name = tracker.get_slot("name")
#         # usermail = tracker.get_slot("usermail")
#         print("action2")
#         DataUpdate(name,questionquery)
#         return[]
    
class DisplaywebAction(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nlp = spacy.load("en_core_web_md")
        user_input = tracker.latest_message.get("text")
        doc = nlp(user_input)
        openai.api_key=os.getenv('api')
        completions=openai.Completion.create(engine='text-davinci-002',prompt=user_input,max_tokens=1500)
        message=completions.choices[0].text
        answer=message
        print(answer)
        dispatcher.utter_message(answer)
        DataUpdate(user_input,answer)
        print(user_input)
        return[]