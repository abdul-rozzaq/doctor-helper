from math import atan2, cos, radians, sin, sqrt

from bot import send_with_bot


def send_otp_code(number: str, code: int):
    """
    OTP uchun sms yuborish funksiyasi
    #! Qayta yozish kerak
    """

    message = f"{number} : {code}"

    return send_with_bot(message)


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
