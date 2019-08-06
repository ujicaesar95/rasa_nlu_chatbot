from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa.core.domain import Domain
from rasa.core.trackers import Eventverbosity

import logging
logger = logging.getLogger(__name__)

from rasa.core.sdk import Action
from rasa.core.sdk.events import SlotSet
from rasa.core.sdk.events import UserUtteranceReverted
from rasa.core.sdk.events import AllSlotsReset
from rasa.core.sdk.events import Restarted

class SaveConfirmDoctor(Action):
    def name(self):
        return 'action_save_confirm_doctor'
    
    def run(self, dispatcher, tracker, domain):
        confirm_doctor = next(tracker.get_latest_entity_values("confirm_doctor_entity"), None)
        if not confirm_doctor:
            dispatcher.utter_message("maaf nama dokter itu tidak tersedia, mohon pilih salah satu dokter dari list tersebut")
            return[UserUtteranceReverted()]
        return [SlotSet('confirm_doctor_entity',confirm_doctor)]
    
class SaveUserName(Action):
    def name(self):
        return 'action_save_user_name'
    
    def run(self, dispatcher, tracker, domain):
        user_name = next(tracker.get_latest_entity_values("user_name_entity"), None)
        return[SlotSet('user_name_entity'), user_name]

class SaveSymptomp(Action):
    def name(self):
        return 'action_save_symptomp'
    
    def run(self, dispatcher, tracker, domain):
        symptomp = next(tracker.get_latest_entity_values("symptomp_entity"), None)
        if not symptomp:
            dispatcher.utter_message("maaf symptomp tersebut tidak saya kenali, mohon pilih symptomp yang lain")
            return[UserUtteranceReverted()]
        return[SlotSet('symptomp_entity'), symptomp]

class SaveSymptompDuration(Action):
    def name(self):
        return 'action_save_symptomp_duration'

    def run(self, dispatcher, tracker, domain):
        symptompDuration = next(tracker.get_latest_entity_values("symptompDuration_entity"), None)
        if not symptompDuration:
            dispatcher.utter_message("maaf durasi symptomp tersebut tidak saya kenali, mohon pilih durasi symptomp yang lain")
            return[UserUtteranceReverted()]
        return[SlotSet('symptompDuration_entity'), symptompDuration]

class SaveAppointmentSchedule():
    def name(self):
        return 'action_save_appointment_schedule'
    
    def run(self, dispatcher, tracker, domain):
        appointmentSchedule = next(tracker.get_latest_entity_values("appointmentSchedule_entity"), None)
        if not appointmentSchedule:
            dispatcher.utter_message("maaf waktu tersebut tidak tersedia, mohon pilih waktu yang lain")
            return[UserUtteranceReverted()]
        return[SlotSet('appointmentSchedule_entity'), appointmentSchedule]

class SaveAppointmentPlace():
    def name(self):
        return 'action_save_appointment_place'

    def run(self, dispatcher, tracker, domain):
        appointmentPlace = next(tracker.get_latest_entity_values("appointmentPlace_entity"), None)
        if not appointmentPlace:
            dispatcher.utter_message("maaf tempat tersebut tidak tersedia, mohon pilih tempat yang lain")
            return[UserUtteranceReverted()]
        return[SlotSet('appointmentPlace_entity'), appointmentPlace ]


    