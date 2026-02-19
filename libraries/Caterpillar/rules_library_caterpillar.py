rule_sets = {
    "1": {
        "name": "AR",
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
            (r'\bCAT Certified Maintained\b', r'<phoneme alphabet="ipa" ph="kˈat‿ˈsɝ.tɪ.faɪd‿meɪnˈteɪnd">CAT Certified Maintained</phoneme>'),
            (r'\bCVA\b', r'C-V-A'),
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
        "name": "zh-CN",
        "rules": [
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\b均包含\b', r'<phoneme alphabet="sapi" ph="jun 1 - bao 1 - han 2">均包含</phoneme>'),
            (r'\b维修两日毕\b', r'<phoneme alphabet="sapi" ph="wei 2 - xiu 1 - liang 3 - ri 4 - bi 4">维修两日毕</phoneme>'),
            (r'\b设备拥有\b', r'<phoneme alphabet="sapi" ph="she 4 - bei 4 - yong 3 - you 3">设备拥有</phoneme>'),
        ]
    },
    "11": {
        "name": "zh-TW",
        "rules": [
            (r'\b鏟斗\b', r'<phoneme alphabet="sapi" ph="ㄔㄢˇ ㄉㄡˇ ">鏟斗</phoneme>'),
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\b為\b', r'<phoneme alphabet="sapi" ph="ㄨㄟˊ ">為</phoneme>'),
        ]
    },
    "12": {
        "name": "de-DE",
        "rules": [
            (r'\bCVAs\b', r'<phoneme alphabet="ipa" ph="tseːfaʊ̯ˈas">CVAs</phoneme>'),
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\bCat Certified Maintained\b', r'<lang xml:lang="en-US">Cat Certified Maintained</lang>'),
            (r'\bVisionLink\b', r'<lang xml:lang="en-US">VisionLink</lang>'),
        ]
    },
    "13": {
        "name": "es-MX",
        "rules": [
            (r'\bCat Certified Maintained\b', r'<lang xml:lang="en-US">Cat Certified Maintained</lang>'),
            (r'\bCat Inspect\b', r'<lang xml:lang="en-US">Cat Inspect</lang>'),
            (r'\bVisionLink\b', r'<lang xml:lang="en-US">VisionLink</lang>'),
            (r'\bcuándo\b', r'<phoneme alphabet="ipa" ph="kuˈando">cuándo</phoneme>'),
            (r'\bdónde\b', r'<phoneme alphabet="ipa" ph="dˈondˌe">dónde</phoneme>'),
            (r'\bqué\b', r'<phoneme alphabet="ipa" ph="kˈe">qué</phoneme>'),
        ]
    },
    "14": {
        "name": "fr-FR",
        "rules": [
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\bCat Certified Maintained\b', r'<lang xml:lang="en-US">Cat Certified Maintained</lang>'),
        ]
    },
}
