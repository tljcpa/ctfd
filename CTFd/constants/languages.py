from CTFd.constants import RawEnum


class Languages(str, RawEnum):
    ENGLISH = "en"
    GERMAN = "de"
    POLISH = "pl"


LANGUAGE_NAMES = {
    "en": "English",
    "de": "Deutsch",
    "pl": "Polski",
}

SELECT_LANGUAGE_LIST = [("", "")] + [
    (str(lang), LANGUAGE_NAMES.get(str(lang))) for lang in Languages
]
