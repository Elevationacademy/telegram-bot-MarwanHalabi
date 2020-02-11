import requests

TOKEN = '1090954125:AAHA-WX4zsCnVr9pcm2nRXuwuuXDqaM1cQA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://60995f92.ngrok.io/message' \
    .format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

def check_func(message):
    messageL = message['text'].split()
    if messageL[0] == "check":
        try:
            msg = is_prime(messageL[1])
            res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                               .format(TOKEN, message['chat']['id'], msg))
        except:
            pass


def is_prime(num):
    num = int(num)  # TODO check if int
    if num > 1:
        if (num % 2 == 0) & (num != 2):
            return "Come on dude, you know even numbers are not prime!"
        for i in range(2, num):
            if (num % i) == 0:
                return "not prime"
        else:
            return "prime"
    else:
        return "not prime"


def fact_func(message):
    messageL = message['text'].split()
    if messageL[0] == "factorial":
        try:
            msg = is_fact(messageL[1])
            res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                               .format(TOKEN, message['chat']['id'], msg))
        except:
            pass


def is_fact(num):
    num = int(num)
    i = f = 1
    while f < num:
        i += 1
        f *= i
    if f == num:
        return "is factorial"
    else:
        return "is not factorial"


def reverse_str(s):
    return s[::-1]


def is_Palindrome(s):
    rev = reverse_str(s)
    if s == rev:
        return "is Palindrome"
    return "is not Palindrome"


def Palindrome_func(message):
    messageL = message['text'].split()
    if messageL[0] == "palindrome":
        try:
            msg = is_Palindrome(messageL[1])
            res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                               .format(TOKEN, message['chat']['id'], msg))
        except:
            pass