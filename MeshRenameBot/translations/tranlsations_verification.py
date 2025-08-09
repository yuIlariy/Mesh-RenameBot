from en import EnglishTranslations
from es import SpanishTranslations
from ar import ArabicTranslations
from hi import HindiTranslations
from ko import KoreanTranslations
from ru import RussianTranslations
from zh import ChineseTranslations
from fr import FrenchTranslations
from pt import PortugueseTranslations

for directive in dir(EnglishTranslations):
    if directive.startswith("__"):
        continue
    for translation in [
        ArabicTranslations,
        ChineseTranslations,
        HindiTranslations,
        KoreanTranslations,
        RussianTranslations,
        SpanishTranslations,
        FrenchTranslations,
        PortugueseTranslations,
    ]:
        if not hasattr(translation, directive):
            print(f"Missing {directive} in {translation.__name__}")
