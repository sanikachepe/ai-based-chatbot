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

class FacilityForm(FormAction):

    def name(self) -> Text:
        # unique identifier of the form

        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        # A list of required slots that the form has to fill
        return ["facility_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                 intent=["inform", "search_provider"]),
               "location": self.from_entity(entity="location",
                                            intent=["inform", "search_provider"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
               ) -> List[Dict]:
        location = tracker.get_slot('location')
        facility_type = tracker.get_slot('facility_type')

        results = _find_facilities(location, facility_type)
        button_name = _resolve_name(FACILITY_TYPES, facility_type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry we could not find a {} in {}.".format(button_name, location.title()))

            return[]

        buttons = []
        for r in results[:3]:
            if facility_type == FACILITY_TYPES["hospital"]["resource"]:



