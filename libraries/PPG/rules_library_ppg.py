rule_sets = {
    "1": {
        "name": "French (Canada)",
        "rules": [
            (r'\bchevauchement\b', r'<phoneme alphabet="ipa" ph="ʃə.voʃ.mɑ̃">chevauchement</phoneme>'),
            (r'(?-i:\bEst\b)(?!-)', r'<phoneme alphabet="ipa" ph="ˈeste">Est</phoneme>'),  # case-sensitive and not 'Est-ce': skips the verb 'est'
            (r'\btous\b(?!\s+(?:les|ces|ceux|mes|tes|ses|nos|vos|leurs|deux|trois|types|genres|usages|supports|azimuts|terrains|temps)\b)', r'<phoneme alphabet="ipa" ph="tʊs">tous</phoneme>'),
            (r"(?<!\bplus )\b(en) plus\b(?=\s*[,.;:!?)<]|\s+d(?:e|u|es)\b|\s+d['’])", r'\1 <phoneme alphabet="ipa" ph="plys">plus</phoneme>'),  # 'en plus' (= in addition) only: the s is silent in 'ne ... plus', 'plus rapide'
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
