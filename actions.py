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
from rasa_sdk.events import AllSlotsReset
from weather import get_weather
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict
import requests
#import openpyxl
import re
import datetime
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

        location = tracker.get_slot("location")
        dispatcher.utter_message(text="Facility Search Action!")

        return [AllSlotsReset()]

#checking 

class ActionDrivingLicense(Action):

    def name(self) -> Text:
         return "action_driving_license_form"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         age = tracker.get_slot("age")    
         location = tracker.get_slot("location")
         int_age = int(age)
         #flag_ll = False 
         flag_dl = False

         message ="" 
         if int_age < 16:
           message = "sorry, you aren't eligible for license "
         elif int_age >=16 and int_age <18    :
           message= "you can apply for learner’s licence for Motorcycles without gear with capacity up to 50cc and require parent’s or guardian’s permission "
         else :
           message = "you are eligible for license "
           flag_dl = True

         final_message = message + "in " + location  #check location and age
         
         dispatcher.utter_message(text= final_message)

         if flag_dl == True:
           
             dispatcher.utter_message(text = """How to submit your driving licence application form
                          • Visit the Sarathi website of the Ministry of Road Transport and Highways.
                          • On your left hand side, you will see options under “Driving Licence”.
                          • Choose “Apply Online” option and from the drop down choose “New Driving Licence”.
                          • You will now see instructions for submitting your driving licence application form. Please read the instructions carefully and click on the “Continue” button to proceed.
                          • Once you click on the “Continue” button, will be asked if you are holding a Learner’s Licence, a Foreign DL, or a Defence Licence. Tick the appropriate box and proceed.
                          • Based on what you selected above, you will be asked for the Learner’s Licence Number/Foreign DL NUmber/ Defence Licence Number.
                          • You will also be asked to enter your date of birth in DDMMYYYY format.
                          • Once you fill the information asked, please click on “OK”.
                          • In this form, you will be asked to fill up your personal details like your name, age, and address.
                          • Once you click on all the details, you will be asked to upload all the required supporting documents like address proof, age proof, and identity proof.
                          • You may be asked to upload a passport size photograph and your signature. Please keep the scanned copies for the same ready.
                          • Once you have uploaded all the documents, you will be asked to choose the timing for your DL appointment. Please select the date and the time when you will be available to go directly to the RTO and appear for your DL test.
                          • Once you make the payment to submit your driving licence application form, your application will be successfully sent to the RTO.
                          • On your appointment day, make sure you reach few minutes early and give your test.
                      The section is to be signed in the presence of the Licensing Authority by the parent/guardian.
                      On completion of the form and after reviewing the information, the applicant can submit the form online by clicking on the 'Submit' button at the end of the form.
                      On submission, an auto-generated Web Application Number will appear on screen. Note the number for future reference and to check the status of the application.""")           
            # FollowupAction("action_followup_check")
             flag_dl = False

         return [AllSlotsReset()]


class ActionLearnersLicense(Action):

    def name(self) -> Text:
         return "action_learners_license_form"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         age = tracker.get_slot("age")    
         location = tracker.get_slot("location")
         int_age = int(age)
         flag_ll = False 
         

         message ="" 
         if int_age < 16:
           message = "sorry, you aren't eligible for license "
         elif int_age >=16 and int_age <18    :
           message= "you can apply for learner’s licence for Motorcycles without gear with capacity up to 50cc and require parent’s or guardian’s permission "
           flag_ll = True
         else :
           message = "you are eligible for learners license "
           flag_ll = True

         final_message = message + "in " + location  
         
        # print(final_message) 
         dispatcher.utter_message(text= final_message)

         if flag_ll == True:
             dispatcher.utter_message(text ="""Steps to get Learner’s licence: 
                         
                        1) you need to register on your district’s RTO website by filling the application forms
                        2) visit the nearest RTO to submit the application
                        3) register on parivahan.gov.in for test
                        4) visit RT office for test
                        5) On passing the test, the learner’s licence will be sent to your permanent address.
                         """) 
             flag_ll = False

         return [AllSlotsReset()]


class ActionFollowCheck(Action):

    def name(self) -> Text:
        return "action_followup_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="this is action after true")
        print("Followup action running")

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


class ActionRestart(Action):

  def name(self) -> Text:
      return "action_restart"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:

      # custom behavior

      return []

# class ActionPoliceStation(Action):

#     def name(self) -> Text:
#          return "action_police_station"

#     def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
#          location = tracker.get_slot("location")           

        
#          message = "police station contact number : 100 "
#          final_message = message + "in " + location  
         
#         # print(final_message) 
#          dispatcher.utter_message(text= final_message)

             

#          return [AllSlotsReset()]




class PoliceNumbers(Action):
    def name(self) -> Text:
        return "police_number_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "state","location","problem"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

      
        dispatcher.utter_message(template="utter_details_thanks", Name=tracker.get_slot("name"),
                                                                 State=tracker.get_slot("state"),
                                                                 City=tracker.get_slot("location"))
                                                            

                                 
        maharashtra = {"mumbai": {"police" : "022-22621855",
                    "ambulance" : "1298/ 022-24308888",
                    "fire": "022-23085991 / 992",
                    "women helpline": "022-22633333/ 22620111"},
                "pune": {"police" : " 020-26126296/ 26122880",
                    "ambulance" : "108",
                    "fire": "101",
                    "women helpline": "1091"},
                "nagpur": {"police" : "0712-2561222 ",
                    "ambulance" : "108",
                    "fire": "101",
                    "women helpline": "1091"}}
               

        if tracker.get_slot("state") == "maharashtra":
       
            j = tracker.get_slot("location")
            k = tracker.get_slot("problem")
            message_print = "the number for " + k + " in " + j + " is " + maharashtra[j][k]
            dispatcher.utter_message(text= message_print )
 #-------------------------------------------------------------------------            

#other fir form
class ReportFIROtherForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","problem"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

         


        dispatcher.utter_message(text = tracker.get_slot("name")+ "hi")
        return [AllSlotsReset()]
 #-------------------------------------------------------------------------
# vehicle theft form
class ReportFIROvehicletheftForm(Action):
    def name(self) -> Text:
        return "theft_of_vehicle_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","problem","vehicle","number_plate","colour","last_seen","anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir3"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

          

        dispatcher.utter_message(text = "thank you for the information ," + tracker.get_slot("name"))
        return [AllSlotsReset()]
 #-------------------------------------------------------------------------        
#theft form

class ReportFIRgoodstheftForm(Action):
    def name(self) -> Text:
        return "theft_of_goods_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","goods_stolen","date_time","last_seen","anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir4"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:


       

        dispatcher.utter_message(text = "thank you for the information ," + tracker.get_slot("name"))
        return [AllSlotsReset()] 
 #-------------------------------------------------------------------------

class ReportFIRMissingPersonForm(Action):
    def name(self) -> Text:
        return "missing_person_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","name_of_missing_person","age_of_mm","sex","clothes_of_mm","last_seen","anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir5"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

           

        dispatcher.utter_message(text = "thank you for the information ," + tracker.get_slot("name"))
        return [AllSlotsReset()]   
 #-------------------------------------------------------------------------                                                    

class ReportLostandFoundForm(Action):
    def name(self) -> Text:
        return "lost_and_found_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","lost_or_found","item_lost_or_found","location_of_item","anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir6"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

           

        dispatcher.utter_message(text = "thank you for the information ," + tracker.get_slot("name"))
        return [AllSlotsReset()]  
#-------------------------------------------------------------------------        

class ReportAssaultForm(Action):
    def name(self) -> Text:
        return "assault_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","email", "dob","complaint_against","assault_description","anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_fir7"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

           

        dispatcher.utter_message(text = "thank you for the information ," + tracker.get_slot("name"))
        return [AllSlotsReset()]  
#-------------------------------------------------------------------------        


class ReportCivicGrievanceForm(Action):
    def name(self) -> Text:
        return "civic_grievance_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:
        required_slots = ["name", "mobile_no","aadhar_no","civic_grievance", "location","state", "landmark", "anything_else"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
                

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit_cg"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

         


        dispatcher.utter_message(text = "thank you for the information, " + tracker.get_slot("name"))
        return [AllSlotsReset()]

#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateUserDetailsForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_user_details_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_problem(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `problem` value."""

        # If the problem is super short, it might be wrong.
        print(f"problem = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"problem": None}
        else:
            return {"problem": slot_value}        

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}
#--------------------------------------------------------------------------
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        #aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (tracker.get_slot('aadhar_no') == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, tracker.get_slot('aadhar_no'))):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------


#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateTheftOfVehicleForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_theft_of_vehicle_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_vehicle(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `vehicle` value."""

        # If the problem is super short, it might be wrong.
        print(f"vehicle = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"vehicle": None}
        else:
            return {"vehicle": slot_value}     

#--------------------------------------------------------------------------
    def validate_colour(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `colour` value."""

        # If the problem is super short, it might be wrong.
        print(f"vehicle = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's very short. I'm assuming you mis-spelled")
            return {"colour": None}
        else:
            return {"colour": slot_value}                    

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}
#--------------------------------------------------------------------------

    def validate_last_seen(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last seen` value."""

        # If the name is super short, it might be wrong.
        print(f"last seen = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"last_seen": None}
        else:
            return {"last_seen": slot_value}

#--------------------------------------------------------------------------           
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

#--------------------------------------------------------------------------
    def validate_number_plate(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `number plate` value."""

        print(f"vehicle identification number given = {slot_value}")
        number_plate = tracker.get_slot('number_plate')
        regex = ("^([A-Z|a-z]{2}\s{1}\d{2}\s{1}[A-Z|a-z]{1,2}\s{1}\d{1,4})?([A-Z|a-z]{3}\s{1}\d{1,4})?$")

        p = re.compile(regex)

        if (number_plate == None):
            dispatcher.utter_message(text=f"Please enter a valid vehicle identification number.")
            return {"number_plate": None}

        if (re.search(p, number_plate)):
            return {"number_plate": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid vehicle identification number.")
            return {"number_plate": None}            
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------


#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateTheftOfGoodsForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_theft_of_goods_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_goods_stolen(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `goods_stolen` value."""

        # If the problem is super short, it might be wrong.
        print(f"goods_stolen = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"goods_stolen": None}
        else:
            return {"goods_stolen": slot_value}     
          

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}
#--------------------------------------------------------------------------

    def validate_last_seen(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last seen` value."""

        # If the name is super short, it might be wrong.
        print(f"last seen = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"last_seen": None}
        else:
            return {"last_seen": slot_value}

#--------------------------------------------------------------------------           
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
   
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateMissingPersonForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_missing_person_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_name_of_missing_person(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name of missing person` value."""

        # If the problem is super short, it might be wrong.
        print(f"name_of_missing_person = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name_of_missing_person": None}
        else:
            return {"name_of_missing_person": slot_value}     

#--------------------------------------------------------------------------
    def validate_colour_of_mm(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name of missing person` value."""

        # If the problem is super short, it might be wrong.
        print(f"colour of clothes = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's very vague. please provide more details")
            return {"colour_of_mm": None}
        else:
            return {"colour_of_mm": slot_value}                 
          

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}
#--------------------------------------------------------------------------

    def validate_last_seen(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last seen` value."""

        # If the name is super short, it might be wrong.
        print(f"last seen = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"last_seen": None}
        else:
            return {"last_seen": slot_value}

#--------------------------------------------------------------------------           
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
   
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------

# lost and found form

class ValidateLostAndFoundForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_lost_and_found_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_item_lost_or_found(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name of missing person` value."""

        # If the problem is super short, it might be wrong.
        print(f"item_lost_or_found = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"item_lost_or_found": None}
        else:
            return {"item_lost_or_found": slot_value}     

#--------------------------------------------------------------------------
    def validate_location_of_item(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name of missing person` value."""

        # If the problem is super short, it might be wrong.
        print(f"location_of_item = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's very vague. please provide more details")
            return {"location_of_item": None}
        else:
            return {"location_of_item": slot_value}                 
          

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}

#--------------------------------------------------------------------------           
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
   
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------

#assault fir validation

#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateAssaultFirForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_assault_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------

    def validate_complaint_against(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"complaint_against = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"complaint_against": None}
        else:
            return {"complaint_against": slot_value}
#--------------------------------------------------------------------------
    def validate_assault_description(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `assault_description` value."""

        # If the problem is super short, it might be wrong.
        print(f"assault_description = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"assault_description": None}
        else:
            return {"assault_description": slot_value}        

#--------------------------------------------------------------------------
    def validate_dob(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `dob` value."""

        print(f"dob given = {slot_value}")
        
        today = datetime.datetime.now()
        age = tracker.get_slot('age')
        present_year = today.year
        date_str = tracker.get_slot('dob')
        format_str = '%d-%m-%Y'  # The format
        try:
            datetime_obj = datetime.datetime.strptime(date_str, format_str)
            input_year = datetime_obj.year
            print(datetime_obj.date())
            return {"dob": slot_value}
        except ValueError:
            print("incorrect date format")
            dispatcher.utter_message(text="Seems like you have entered your date of birth in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
            return {"dob": None}
#--------------------------------------------------------------------------
    def validate_current_address(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `address` value."""

        # If the name is super short, it might be wrong.
        print(f"address given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short address. I'm assuming you mis-spelled.")
            return {"current_address": None}
        else:
            return {"current_address": slot_value}
#--------------------------------------------------------------------------
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------
# civic grievance validation

#-------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

class ValidateCivicGrievanceForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_civic_grievance_form"

    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}
#--------------------------------------------------------------------------
    def validate_grievance(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `problem` value."""

        # If the problem is super short, it might be wrong.
        print(f"grievance = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"grievance": None}
        else:
            return {"grievance": slot_value}        



#--------------------------------------------------------------------------
    def validate_landmark(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `landmark` value."""

        # If the problem is super short, it might be wrong.
        print(f"landmark = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 8:
            dispatcher.utter_message(text=f"That's a little vague. Please provide more details")
            return {"landmark": None}
        else:
            return {"landmark": slot_value}        



#--------------------------------------------------------------------------
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile_no` value."""

        print(f"email given = {slot_value}")
        email = tracker.get_slot('email')
        regex = ("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

        p = re.compile(regex)

        if (email == None):
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}

        if (re.search(p, email)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email.")
            return {"email": None}
#--------------------------------------------------------------------------

    def validate_mobile_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `mobile no` value."""

        print(f"phone number given = {slot_value}")
        phone = tracker.get_slot('mobile_no')
        regex = ("^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$")

        p = re.compile(regex)

        if (phone == None):
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

        if (re.search(p, phone)):
            return {"mobile_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid phone number.")
            return {"mobile_no": None}

#--------------------------------------------------------------------------


    def validate_aadhar_no(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `aadhar_no` value."""

        print(f"aadhar_no number given = {slot_value}")
        aadhar_no = tracker.get_slot('aadhar_no')
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                 "s[0-9]{4}\\s[0-9]{4}$")

        p = re.compile(regex)

        if (aadhar_no == None):
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}

        if (re.search(p, aadhar_no)):
            return {"aadhar_no": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
            return {"aadhar_no": None}
#--------------------------------------------------------------------------------


    # def validate_city(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `first_name` value."""

    #     print(f"city given = {slot_value}")
    #     file = "IndianCitiesDb.xlsx"
    #     wb = openpyxl.load_workbook(file, read_only=True)
    #     ws = wb.active
    #     state_of_city = ""
    #     city = tracker.get_slot('city')
    #     for row in ws.iter_rows(min_row=1, min_col=1, max_row=214, max_col=1):
    #         for cell in row:
    #             if cell.value == city.title():
    #                 state_of_city = ws.cell(row=cell.row, column=2).value

    #     if state_of_city == "":
    #         dispatcher.utter_message(text=f"Seems like you have mis-spelled. Please enter a correct city name.")
    #         return {"city": None}
    #     else:
    #         print(state_of_city)
    #         SlotSet("state_for_license", state_of_city)
    #         return {"city": slot_value}

    # def validate_pin_code(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `pin_code` value."""

    #     print(f"pin code given = {slot_value} length = {len(slot_value)}")
    #     pin_code = tracker.get_slot('pin_code')
    #     final_url = f"https://api.postalpincode.in/pincode/" + pin_code
    #     pin_data = requests.get(final_url).json()
    #     if len(slot_value) != 6:
    #         dispatcher.utter_message(text=f"Seems like you have entered an incorrect pin code. A pin code must be of 6 digits.")
    #         return {"pin_code": None}
    #     else:
    #         if pin_data[0]['Status'] == 'Success' and pin_data[0]['PostOffice'][0]['District'] == tracker.get_slot('city').title():
    #             return {"pin_code": slot_value}
    #         else:
    #             dispatcher.utter_message(text=f"Seems like you have entered an incorrect pin code or your pin code doesn't match your city. Please enter a valid pin code.")
    #             return {"pin_code": None}
#--------------------------------------------------------------------------
 
    # def validate_aadhar_no(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `aadhar_no` value."""

    #     print(f"aadhar_no number given = {slot_value}")
    #     aadhar_no = tracker.get_slot('aadhar_no')
    #     regex = ("^[2-9]{1}[0-9]{3}\\" +
    #              "s[0-9]{4}\\s[0-9]{4}$")

    #     p = re.compile(regex)

    #     if (aadhar_no == None):
    #         dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
    #         return {"aadhar_no": None}

    #     if (re.search(p, aadhar_no)):
    #         return {"aadhar_no": slot_value}
    #     else:
    #         dispatcher.utter_message(text=f"Please enter a valid 12-digit aadhar_no number in XXXX XXXX XXXX format.")
    #         return {"aadhar_no": None}

    # def validate_date_for_appointment(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `date_for_appointment` value."""

    #     print(f"appointment date given = {slot_value}")
    #     today = datetime.datetime.now()
    #     date_str = tracker.get_slot('date_for_appointment')
    #     format_str = '%d-%m-%Y'  # The format
    #     try:
    #         datetime_obj = datetime.datetime.strptime(date_str, format_str)
    #         input_year = datetime_obj.year
    #         print(datetime_obj.date())
    #         if datetime_obj.date() < today.date():
    #             dispatcher.utter_message(text="Seems like you have entered an incorrect date. Please enter a valid date.")
    #             return {"date_for_appointment": None}
    #         elif datetime_obj.weekday() == 6:
    #             dispatcher.utter_message(text="Sorry, we are closed on Sunday, please choose another date.")
    #             return {"date_for_appointment": None}
    #         else:
    #             return {"date_for_appointment": slot_value}
    #     except ValueError:
    #         print("incorrect date format")
    #         dispatcher.utter_message(text="Seems like you have entered the date in the incorrect format or have entered an incorrect date. Please use DD-MM-YYYY format and enter a valid date.")
    #         return {"date_for_appointment": None}

    # def validate_slot_for_appointment(
    #         self,
    #         slot_value: Any,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `slot_for_appointment` value."""

    #     selected_slot = tracker.get_slot('slot_for_appointment')
    #     print(f"slot name given = {slot_value}")
    #     if selected_slot != "10.00 to 12.00" and selected_slot != "12.30 to 14.30" and selected_slot != "15.00 to 17.00":
    #         dispatcher.utter_message(text=f"Please enter a valid slot.")
    #         return {"slot_for_appointment": None}
    #     else:
    #         return {"slot_for_appointment": slot_value}



# class ReportFIRMissingPersonForm(Action):
#     def name(self) -> Text:
#         return "missing_person_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[Dict[Text, Any]]:
#         required_slots = ["name", "state","problem","location","email", "dob"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
                

#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]

# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit_fir"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:

#         # Name = tracker.get_slot("name")
#         # State = tracker.get_slot("state")
#         # Problem = tracker.get_slot("problem")
#         dispatcher.utter_message(template="utter_details_thanks", Name=tracker.get_slot("name"),
#                                                                  State=tracker.get_slot("state"),
#                                                                  Problem=tracker.get_slot("problem"),
#                                                                  City=tracker.get_slot("location"))
                                                            

                                                                                  



    


