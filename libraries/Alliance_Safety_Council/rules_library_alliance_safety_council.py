rule_sets = {
    "1": {
        "name": "Spanish",
        "rules": [
          (r'\(?(1)?\)?([-. ]?\d{3}[-. ]\d{3}[-. ]\d{4})', r'<say-as interpret-as="telephone">\1\2</say-as>'),
          (r'\bWaskey\b', r'Wáskey'),
          (r'\bANSI\b', r'Ansi'),
          (r'\bSDS\b', r'<say-as interpret-as="characters">SDS</say-as>'),
          (r'\bJSEA\b', r'<say-as interpret-as="characters">JSEA</say-as>'),
          (r'\bOsha\b', r'<phoneme alphabet="ipa" ph="ˈoʃa">Osha</phoneme>'),
          (r'\bPenhall\b', r'<phoneme alphabet="ipa" ph="pˈɛn.hɔl">Penhall</phoneme>'),
          (r'\bProcedure\b', r'<phoneme alphabet="ipa" ph="proˈsidʒur">Procedure</phoneme>'),
          (r'\bcause\b', r'<phoneme alphabet="ipa" ph="ˈkau.se">cause</phoneme>'),
          (r'\bOrion\b', r'<phoneme alphabet="ipa" ph="oˈɾai.on">Orion</phoneme>'),
          (r'\bEngineered\b', r'<phoneme alphabet="ipa" ph="ˌendʒiˈnieɾd">Engineered</phoneme>'),
          (r'\bEscanee\b', r'escané-e'),
        ]
    }
}
