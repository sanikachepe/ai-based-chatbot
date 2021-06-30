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
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset
import requests

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
        # entities = tracker.latest_message['entities']
        dispatcher.utter_message(text="Facility Search Action!")

        return []

class ActionWeather(Action):

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

# class ActionDrivingLicense(Action):
#
#     def name(self) -> Text:
#         return "action_driving_license_form"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         age = tracker.get_slot("age")
#         location = tracker.get_slot("location")
#         int_age = int(age)
#         # flag_ll = False
#         flag_dl = False
#
#         message = ""
#         if int_age < 16:
#             message = "sorry, you aren't eligible for license "
#         elif int_age >= 16 and int_age < 18:
#             message = "you can apply for learner’s licence for Motorcycles without gear with capacity up to 50cc and require parent’s or guardian’s permission "
#         else:
#             message = "you are eligible for license "
#             flag_dl = True
#
#         final_message = message + "in " + location  # check location and age
#
#         dispatcher.utter_message(text=final_message)
#
#         if flag_dl == True:
#             dispatcher.utter_message(text="""How to submit your driving licence application form
#                           • Visit the Sarathi website of the Ministry of Road Transport and Highways.
#                           • On your left hand side, you will see options under “Driving Licence”.
#                           • Choose “Apply Online” option and from the drop down choose “New Driving Licence”.
#                           • You will now see instructions for submitting your driving licence application form. Please read the instructions carefully and click on the “Continue” button to proceed.
#                           • Once you click on the “Continue” button, will be asked if you are holding a Learner’s Licence, a Foreign DL, or a Defence Licence. Tick the appropriate box and proceed.
#                           • Based on what you selected above, you will be asked for the Learner’s Licence Number/Foreign DL NUmber/ Defence Licence Number.
#                           • You will also be asked to enter your date of birth in DDMMYYYY format.
#                           • Once you fill the information asked, please click on “OK”.
#                           • In this form, you will be asked to fill up your personal details like your name, age, and address.
#                           • Once you click on all the details, you will be asked to upload all the required supporting documents like address proof, age proof, and identity proof.
#                           • You may be asked to upload a passport size photograph and your signature. Please keep the scanned copies for the same ready.
#                           • Once you have uploaded all the documents, you will be asked to choose the timing for your DL appointment. Please select the date and the time when you will be available to go directly to the RTO and appear for your DL test.
#                           • Once you make the payment to submit your driving licence application form, your application will be successfully sent to the RTO.
#                           • On your appointment day, make sure you reach few minutes early and give your test.
#                       The section is to be signed in the presence of the Licensing Authority by the parent/guardian.
#                       On completion of the form and after reviewing the information, the applicant can submit the form online by clicking on the 'Submit' button at the end of the form.
#                       On submission, an auto-generated Web Application Number will appear on screen. Note the number for future reference and to check the status of the application.""")
#             # FollowupAction("action_followup_check")
#             flag_dl = False
#
#         return [AllSlotsReset()]
#
#
# class ActionLearnersLicense(Action):
#
#     def name(self) -> Text:
#         return "action_learners_license_form"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         age = tracker.get_slot("age")
#         location = tracker.get_slot("location")
#         int_age = int(age)
#         flag_ll = False
#
#         message = ""
#         if int_age < 16:
#             message = "sorry, you aren't eligible for license "
#         elif int_age >= 16 and int_age < 18:
#             message = "you can apply for learner’s licence for Motorcycles without gear with capacity up to 50cc and require parent’s or guardian’s permission "
#             flag_ll = True
#         else:
#             message = "you are eligible for learners license "
#             flag_ll = True
#
#         final_message = message + "in " + location
#
#         # print(final_message)
#         dispatcher.utter_message(text=final_message)
#
#         if flag_ll == True:
#             dispatcher.utter_message(text="""Steps to get Learner’s licence:
#
#                         1) you need to register on your district’s RTO website by filling the application forms
#                         2) visit the nearest RTO to submit the application
#                         3) register on parivahan.gov.in for test
#                         4) visit RT office for test
#                         5) On passing the test, the learner’s licence will be sent to your permanent address.
#                          """)
#             flag_ll = False
#
#         return [AllSlotsReset()]
#
#
# class ActionFollowCheck(Action):
#
#     def name(self) -> Text:
#         return "action_followup_check"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="this is action after true")
#         print("Followup action running")
#
#         return []
#
#
# class ActionRestart(Action):
#
#     def name(self) -> Text:
#         return "action_restart"
#
#     async def run(
#             self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # custom behavior
#
#         return []


class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last Message Now ", entities)
        state = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        if state.lower() == "india":
            state = "Total"
        message = "Please enter correct state name"
        for data in response['statewise']:
            if data['state'] == state.title() or data['statecode'] == state.upper():
                message = """Covid19 status in {} is
Active: {}, Confirmed: {}, Recovered: {} On {}""".format(state.title(), data["active"], data["confirmed"], data["recovered"], data["lastupdatedtime"])

        dispatcher.utter_message(message)

        return []
