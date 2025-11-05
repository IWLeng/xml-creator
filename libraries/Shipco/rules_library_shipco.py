rule_sets = {
    "1": {
        "name": "es",
        "rules": [
            (r'\bMy-Pillow\b', r'<lang xml:lang="en-US">My-Pillow</lang>'), 
            (r'\bhackeada\b', r'<phoneme alphabet="ipa" ph="xakeada">hackeada</phoneme>'),
            (r'\bhackeado\b', r'<phoneme alphabet="ipa" ph="xakeado">hackeado</phoneme>'),
            (r'\bhackear\b', r'<phoneme alphabet="ipa" ph="xakear">hackear</phoneme>'),
            (r'\bdeepfakes\b', r'<lang xml:lang="en-US">deepfakes</lang>'),
            (r'\bphishing\b', r'<lang xml:lang="en-US">phishing</lang>'),
            (r'\bTI\b', r'<say-as interpret-as="characters">TI</say-as>'),
        ]
    },
}
