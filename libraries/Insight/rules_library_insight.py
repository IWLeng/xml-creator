rule_sets = {
    "1": {
        "name": "French (Canada)",
        "rules": [
            (r'\bengagement\b', r'<phoneme alphabet="ipa" ph="ɪnˈɡeɪd͡ʒ.mənt">engagement</phoneme>'),
            (r'\bsûr\b', r'<phoneme alphabet="ipa" ph="syʁ">sûr</phoneme>'),
        ]
    },
    "2": {
        "name": "Spanish (Latam)",
        "rules": [
            (r'\boídos\b', r'<phoneme alphabet="ipa" ph="oˈi.dos">oídos</phoneme>'),
            (r'\blisteria\b', r'listéria'),
            (r'\bStandardize\b', r'Stándardais'),
            (r'\bE. coli\b', r'e-coli'),
            (r'', r''),
            (r'', r''),
        ]
    },
    "3": {
      "name": "Portuguese (Brazil)",
      "rules": [
            (r'\bControle\b', r'<phoneme alphabet="ipa" ph="kon.ˈtɾo.li">Controle</phoneme>'),
            (r'\bWhisper\b', r'<lang xml:lang="en-US">Whisper</lang>'),
            (r'\bHershey\b', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ˈhɛrʃi">Hershey</phoneme></lang>'),
            (r'\bmop\b', r'<phoneme alphabet="ipa" ph="mɔ.pi">mop</phoneme>'),
            (r'\bThe Hershey Company\b', r'<lang xml:lang="en-US">The <phoneme alphabet="ipa" ph="ˈhɛrʃi">Hershey</phoneme> Company</lang>'),
            (r'\bHershey Company\b', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ˈhɛrʃi">Hershey</phoneme> Company</lang>'),
            (r'\bDate\b', r'<phoneme alphabet="ipa" ph="da.tʃi">Date</phoneme>'),
            (r'\bTROQUE AS\b', r'<phoneme alphabet="ipa" ph="ˈtɾɔ.ki.as">TROQUE AS</phoneme>'),
            (r'\bHershey Super Six\b', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ˈhɛrʃi">Hershey</phoneme> Super Six</lang>'),
            (r'\bHank\b', r'<lang xml:lang="en-US">Hank</lang>'),
            (r'\bseco\b', r'<phoneme alphabet="ipa" ph="ˈse.ku">seco</phoneme>'),
            (r'\bcóco\b', r'<phoneme alphabet="ipa" ph="ˈko.ku">cóco</phoneme>'),
            (r'\bmonitoram\b', r'<phoneme alphabet="ipa" ph="mo.ni.ˈtɔ.ɾɐ̃w̃">monitoram</phoneme>'),
            (r'\bPC Factory\b', r'<lang xml:lang="en-US">PC Factory</lang>'),
            (r'\bnote\b', r'<phoneme alphabet="ipa" ph="ˈnɔ.tʃi">note</phoneme>'),
      ]
    }
}
