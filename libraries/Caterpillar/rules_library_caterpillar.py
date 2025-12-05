rule_sets = {
    "1": {
        "name": "General",
        "rules": [
            (r'\bDH2\b', r'<say-as interpret-as="characters">DH2</say-as>'),
            (r'\bARM\b', r'<say-as interpret-as="characters">ARM</say-as>'),
        ]
    },
    "2": {
        "name": "es-ES",
        "rules": [
                (r'\bDuo-Cone\b', r'<lang xml:lang="en-US">Duo-Cone</lang>'),
                (r'\bSingle Life Cutting Edges\b', r'<lang xml:lang="en-US">Single Life Cutting Edges</lang>'),
        ]
    },
    "3": {
        "name": "es-LA",
        "rules": [
            (r'\bCone\b', r'<phoneme alphabet="ipa" ph="ˈkoʊn">Cone</phoneme>'),
        ]
    },
    "4": {
        "name": "nl-NL",
        "rules": [
            (r'\bCat\b', r'<phoneme alphabet="ipa" ph="kɑt">Cat</phoneme>'),
            (r'\bCone\b', r'<phoneme alphabet="ipa" ph="ˈkoʊn">Cone</phoneme>'),
        ]
    },
    "5": {
        "name": "pl-PL",
        "rules": [
            (r'\bdealerem\b', r'<phoneme alphabet="ipa" ph="diˈlɛˌrɛm">dealerem</phoneme>'),
        ]
    },
      "6": {
        "name": "pt-BR",
        "rules": [
            (r'\bCat\b', r'</prosody><prosody rate="-20%"><phoneme alphabet="ipa" ph="kˈatʃ">Cat</phoneme></prosody><prosody rate="0%">'),
        ]
    },
      "7": {
        "name": "ru-RU",
        "rules": [
            (r'\bCat\b', r'<lang xml:lang="en-US">Cat</lang>'),
            (r'\bCat Duo Cone\b', r'<lang xml:lang="en-US">Cat Duo Cone</lang>'),
        ]
    },
      "8": {
        "name": "sv-SE",
        "rules": [
            (r'\bhalvpilar\b', r'<phoneme alphabet="ipa" ph="ˈhalvpˌiːlar">halvpilar</phoneme>'),
            (r'\bCat\b', r'<phoneme alphabet="ipa" ph="kat">Cat</phoneme>'),
        ]
    },
      "9": {
        "name": "ja-JP",
        "rules": [
            (r'\bCaterpillar\b', r'<phoneme alphabet="sapi" ph="キャタピラー">Caterpillar</phoneme>'),
        ]
    },
        "10": {
        "name": "zh-TW",
        "rules": [
            (r'\b鏟斗\b', r'<phoneme alphabet="sapi" ph="ㄔㄢˇ ㄉㄡˇ ">鏟斗</phoneme>'),
        ]
    },
}
