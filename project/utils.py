from bot import send_with_bot


def send_otp_code(number: str, code: int):
    """
    OTP uchun sms yuborish funksiyasi
    #! Qayta yozish kerak
    """

    message = f"{number} : {code}"

    return send_with_bot(message)
