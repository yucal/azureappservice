# app/crud/palo_alto.py
from typing import Optional
from app.modules.schemas import senteceCheckRequest
import logging
import random
logging.basicConfig(level=logging.DEBUG)


sentence_dataset = {
    "easy": [
        "Ik wil graag een koffie.",
        "De ober brengt het menu.",
        "Mag ik de rekening, alstublieft?",
        "Ik neem een broodje kaas.",
        "Het eten is lekker.",
        "Ik wil een glas water.",
        "De soep is warm.",
        "Ik zit graag bij het raam.",
        "De ober is vriendelijk.",
        "Het restaurant is mooi."
    ],

    "medium": [
        "Kunt u mij de kaart brengen, alstublieft?",
        "Ik zou graag de dagschotel willen proberen.",
        "Heeft u misschien een vegetarische optie?",
        "De service is vandaag erg snel.",
        "Mag ik wat extra servetten?",
        "De wijn smaakt uitstekend bij de pasta.",
        "Het was erg druk, maar de sfeer was gezellig.",
        "Kunt u de saus apart serveren?",
        "Ik wil graag afrekenen met pin.",
        "De ober vroeg of alles naar wens was."
    ],

    "hard": [
        "Ondanks de drukte bleef het personeel erg attent.",
        "De chef gebruikt lokale producten in zijn gerechten.",
        "Ik waardeer dat er rekening wordt gehouden met mijn allergieën.",
        "De presentatie van het dessert was werkelijk prachtig.",
        "Het restaurant heeft een uitgebreide wijnkaart met verrassende keuzes.",
        "Na afloop kregen we een digestief van het huis aangeboden.",
        "De reservering was per ongeluk dubbel geboekt, maar ze vonden snel een oplossing.",
        "De bediening legde uitgebreid uit hoe het menu samengesteld was.",
        "Het was moeilijk om te kiezen, want alles klonk heerlijk.",
        "De gerechten weerspiegelen echt de seizoenen van Nederland."
    ]
}


def get_sentences():
    logging.debug("Fetching sentences from the data source.")
    # Simulate fetching data
    sentence_hard=random.choice(sentence_dataset["hard"])
    logging.debug(f"Fetched sentences: {sentence_hard}")
    return sentence_hard