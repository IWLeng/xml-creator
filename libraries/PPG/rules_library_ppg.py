rule_sets = {
    "1": {
        "name": "French (Canada)",
        "rules": [
            (r'\bchevauchement\b', r'<phoneme alphabet="ipa" ph="ʃə.voʃ.mɑ̃">chevauchement</phoneme>'),
            (r'\bEst\b', r'<phoneme alphabet="ipa" ph="ˈeste">Est</phoneme>'),
            (r'\btous\b', r'<phoneme alphabet="ipa" ph="tʊs">tous</phoneme>'),
            (r'\bplus\b', r'<phoneme alphabet="ipa" ph="plus">plus</phoneme>'),
            (r'\bCAA\b', r'<say-as interpret-as="characters">CAA</say-as>'),
            (r'\bCOV\b', r'<say-as interpret-as="characters">COV</say-as>'),
            (r'\bTiO2\b', r'<say-as interpret-as="characters">TiO2</say-as>'),
        ]
    },
    "2": {
        "name": "German",
        "rules": [
            (r'\bForeign Object Debris\b', r'<lang xml:lang="en-US">Foreign Object Debris</lang>'),
        ]
    },
}
