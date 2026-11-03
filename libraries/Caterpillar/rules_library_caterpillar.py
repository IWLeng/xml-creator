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
            (r'(?-i:\bIT\b)', r'Ay <phoneme alphabet="ipa" ph="ˈtiː">T</phoneme>'),  # (?-i:...) = case-sensitive
        ]
    },
    "3": {
        "name": "es-LA",
        "rules": [
            (r'\bCone\b', r'<phoneme alphabet="ipa" ph="ˈkoʊn">Cone</phoneme>'),
            (r'\bCAT Certified Maintained\b', r'<phoneme alphabet="ipa" ph="kˈat‿ˈsɝ.tɪ.faɪd‿meɪnˈteɪnd">CAT Certified Maintained</phoneme>'),
            (r'\bCaterpillar\b', r'Cater-pi-larrr'),
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
            (r'\bCat\b(?! Duo Cone\b)', r'<lang xml:lang="en-US">Cat</lang>'),
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
            (r'(?<![A-Za-z0-9_])Caterpillar(?![A-Za-z0-9_])', r'<phoneme alphabet="sapi" ph="キャタピラー">Caterpillar</phoneme>'),  # not \b: kana/kanji count as word characters
        ]
    },
    "10": {
        "name": "zh-CN",
        "rules": [
            (r'(?<![A-Za-z0-9_])CVA(?![A-Za-z0-9_])', r'<say-as interpret-as="characters">CVA</say-as>'),  # not \b: hanzi count as word characters
            (r'均包含', r'<phoneme alphabet="sapi" ph="jun 1 - bao 1 - han 2">均包含</phoneme>'),
            (r'维修两日毕', r'<phoneme alphabet="sapi" ph="wei 2 - xiu 1 - liang 3 - ri 4 - bi 4">维修两日毕</phoneme>'),
            (r'设备拥有', r'<phoneme alphabet="sapi" ph="she 4 - bei 4 - yong 3 - you 3">设备拥有</phoneme>'),
        ]
    },
    "11": {
        "name": "zh-TW",
        "rules": [
            (r'\b為\b', r'<phoneme alphabet="sapi" ph="ㄨㄟˊ ">為</phoneme>'),  # kept first: the tags added below would otherwise make \b match next to 為
            (r'鏟斗', r'<phoneme alphabet="sapi" ph="ㄔㄢˇ ㄉㄡˇ ">鏟斗</phoneme>'),
            (r'(?<![A-Za-z0-9_])CVA(?![A-Za-z0-9_])', r'<say-as interpret-as="characters">CVA</say-as>'),  # not \b: hanzi count as word characters
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
            (r'\bCat Converge\b', r'<lang xml:lang="en-US">Cat Converge</lang>'),
            (r'\bSuite\b', r'<lang xml:lang="en-US">Suite</lang>'),
            (r'\bCustomer Insights\b', r'<lang xml:lang="en-US">Customer Insights</lang>'),
            (r'(?-i:\bSales\b)', r'<lang xml:lang="en-US">Sales</lang>'),  # (?-i:...) = case-sensitive
            (r'\bElizabeth\b', r'<lang xml:lang="en-US">Elizabeth</lang>'),
            (r'\band Marketing\b', r'<lang xml:lang="en-US">and Marketing</lang>'),
            (r'\bCopilot\b', r'<phoneme alphabet="ipa" ph="ˈkoʊˌpaɪlət">Copilot</phoneme>'),
            (r'\bcatdealer\b', r'<lang xml:lang="en-US">cat-dealer</lang>'),
            (r'\bcatconvergesuite\b', r'<lang xml:lang="en-US">cat-converge-suite</lang>'),
            (r'(?<![.,])\b365\b(?![.,]\d)', r'<phoneme alphabet="ipa" ph="tɾesˈsjen.tos seˈsen.ta i ˈsiŋ.ko">365</phoneme>'),  # skips 365,000 and 1,365
            (r'\bCaterpillar\b', r'Caterpí-larr'),
        ]
    },
    "14": {
        "name": "fr-FR",
        "rules": [
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\bCat Certified Maintained\b', r'<lang xml:lang="en-US">Cat Certified Maintained</lang>'),
            (r'\bCat Converge\b', r'<lang xml:lang="en-US">Cat Converge</lang>'),
            (r'\bCustomer Insights\b', r'<lang xml:lang="en-US">Customer Insights</lang>'),
            (r'\bSales and Marketing\b', r'<lang xml:lang="en-US">Sales and Marketing</lang>'),
            (r'\bElizabeth\b', r'<phoneme alphabet="ipa" ph="əlizabɛt">Elizabeth</phoneme>'),
            (r'\band Marketing\b(?!</lang>)', r'<lang xml:lang="en-US">and Marketing</lang>'),  # not inside 'Sales and Marketing' (wrapped above)
            (r'\bCopilot\b', r'<phoneme alphabet="ipa" ph="kɔpilɔt">Copilot</phoneme>'),
            (r'\bcatdealer\b', r'<lang xml:lang="en-US">cat-dealer</lang>'),
            (r'\bcatconvergesuite\b', r'<lang xml:lang="en-US">cat-converge-suite</lang>'),
        ]
    },
    "15": {
        "name": "fr-CA",
        "rules": [
            (r'\bCVA\b', r'<say-as interpret-as="characters">CVA</say-as>'),
            (r'\bparts(?=\.cat\.com\b)', r'<phoneme alphabet="ipa" ph="pɑɹts">parts</phoneme>'),
            (r'\bCat Converge Suite\b', r'<lang xml:lang="en-US">Cat Converge Suite</lang>'),
            (r'\bCustomer Insights\b', r'<lang xml:lang="en-US">Customer Insights</lang>'),
            (r'\bSales and Marketing\b', r'<lang xml:lang="en-US">Sales and Marketing</lang>'),
            (r'\bElizabeth\b', r'<phoneme alphabet="ipa" ph="elizəbəθ">Elizabeth</phoneme>'),
            (r'\bCopilot\b', r'<phoneme alphabet="ipa" ph="kɔpaɪlɔt">Copilot</phoneme>'),
            (r'\bcatdealer\b', r'<lang xml:lang="en-US">cat-dealer</lang>'),
            (r'\bcatconvergesuite\b', r'<lang xml:lang="en-US">cat-converge-suite</lang>'),
            (r'\bMicrosoft Dynamics 365\b', r'<lang xml:lang="en-US">Microsoft Dynamics 365</lang>'),
            (r'(?<=\.com)/(?=[\w<])', r'<phoneme alphabet="ipa" ph="slaʃ">slash</phoneme>'),  # only the slash in a .com/ URL
        ]
    },    
}
