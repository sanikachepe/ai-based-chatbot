# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.events import FollowupAction
#from rasa.core.trackers import DialogueStateTracker

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

class ActionFacilitySearch(Action):

   def name(self) -> Text:
        return "action_facility_search"

   def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        dispatcher.utter_message(text="Facility Search Action!")

        return []



class ActionHelloWorld(Action):

    def name(self) -> Text:
         return "action_driving_license_form"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         age = tracker.get_slot("age")    
         location = tracker.get_slot("location")
         int_age = int(age)
         flag = False 

         message ="" 
         if int_age < 16:
           message = "sorry, you aren't eligible for license "
         elif int_age >=16 and int_age <18    :
           message= "you can apply for lerner’s licence for Motorcycles without gear with capacity up to 50cc and require parent’s or guardian’s permission "
         else :
           message = "you are eligible for license "
           flag = True

         final_message = message + "in " + location  
         
        # print(final_message) 
         dispatcher.utter_message(text= final_message)

         if flag == True:
             dispatcher.utter_message("You need some documents:") 
             FollowupAction("action_followup_check")
             flag = False

         return []


class ActionFollowCheck(Action):

    def name(self) -> Text:
        return "action_followup_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="this is action after true")
        print("Followup action running")

        return []


class ActionRestart(Action):

  def name(self) -> Text:
      return "action_restart"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:

      # custom behavior

      return []

# class ActionGetDrivingLicense(FormAction):
#    def name(self) -> Text:
#        return "driving_license_form"
#
 #   @staticmethod
  #  def required_slots(tracker: Tracker) -> List[Text]:
   #     """A list of required slots"""
#
 #       print("required_slots(tracker: Tracker)")
  #      return ["location", "age"]
#
 #   def submit(self, dispatcher: CollectingDispatcher,
  #          tracker: Tracker,
   #         domain: Dict[Text, Any]) -> List[Dict]:
#
 #       dispatcher.utter_message(text= "hi")
  #      message ="" 
   #     if age < 16:
    #        message = "sorry, you aren't eligible for license "
     #   elif age >=16 && age <18    :
      #      message= "you can apply for lerner's license"
       # else :
        #    message = "you are eligible for license"
#
 #       return[]

    


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