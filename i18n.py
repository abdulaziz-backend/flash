from pathlib import Path
from aiogram.utils.i18n import I18n

def setup_i18n():
    return I18n(path="locales", default_locale="en", domain="messages")