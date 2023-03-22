import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import Voice_Assistant

number = input("Enter your phone number : ")
number = "+91" + number
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carr = carrier.name_for_number(phone, "en")
reges = geocoder.description_for_number(phone, "en")
Voice_Assistant.speak(phone)
Voice_Assistant.speak(time)
Voice_Assistant.speak(carr)
Voice_Assistant.speak(reges)
