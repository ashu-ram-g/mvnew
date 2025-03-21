import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "8115522762:AAGHrL16Ya87K44zxwtVouXbfJwuAy2rYjk"
    # Telegram API ki ID
    API_ID = 21855175
    # Telegram API ki hash key
    API_HASH = "693d541b34acfe8fa0c86278b0c31705"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7973269652'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mewadonlinestudy:yYjxKiZGQag8DnWH@cpvod.ywpecvo.mongodb.net/?retryWrites=true&w=majority&appName=cpvodak"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002526908199
    # Authentication log channel ki ID
    AUTH_LOG = -1002682021662
    # Hit log channel ki ID
    HIT_LOG =-1002472744015
    # DRM dump channel ki ID
    DRM_DUMP = -1002547318739
    # Main channel ki ID
    CHANNEL = -1002565797612
    # Channel ka link
    CH_URL = "https://t.me/+u3QiCOtvBZU3MGQ1"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/ramjikigadi"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

