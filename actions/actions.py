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
# from rasa_sdk.forms import FormAction
from weather import get_weather

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

# class ActionHelloWorld(FormAction):
#
#     def name(self) -> Text:
#         return "admission_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots"""
#
#         print("required_slots(tracker: Tracker)")
#         return ["name", "ssn","subject"]
#
#     def submit(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict]:
#
#         dispatcher.utter_message(template="utter_submit")
#
#         return []


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # entities = tracker.latest_message['entities']
        dispatcher.utter_message(text="Facility Search Action!")

        return []

#
# class GetDrivingLicense(FormAction):
#     def name(self) -> Text:
#         return "driving_license_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots"""
#
#         print("required_slots(tracker: Tracker)")
#         return ["location", "age"]
#
#     def submit(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict]:
#
#         dispatcher.utter_message(text="You have filled the form")
#
#         # if tracker.get_slot(age) < 16:
#         #     dispatcher.utter_message(text="You are not eligible for driving / learner's license :(")
#
#         return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        weather_data = get_weather(city)
        temp = weather_data['main']['temp']
        min_temp = weather_data['main']['temp_min']
        max_temp = weather_data['main']['temp_max']
        desc = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        response = "Weather in {} is {}, Temperature is {} degree Celsius with minimum temperature {} degree Celsius and maximum temperature {} degree Celsius, Humidity is {}%".format(city, desc, temp, min_temp, max_temp, humidity)
        dispatcher.utter_message(response)

        return [SlotSet('location', city)]
