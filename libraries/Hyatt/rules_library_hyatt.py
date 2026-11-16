rule_sets = {
    "1": {
        "name": "de-DE",
        "rules": [
            (r'\bSuite\b', r'<lang xml:lang="en-US">Suite</lang>'),
            (r'\bCourtesy Card\b', r'<lang xml:lang="en-US">Courtesy Card</lang>'),
            (r'\bWorld of Hyatt\b', r'<lang xml:lang="en-US">World of Hyatt</lang>'),
            (r'\bLifetime\b', r'<lang xml:lang="en-US">Lifetime</lang>'),
            (r'\bGlobalist\b', r'<lang xml:lang="en-US">Globalist</lang>'),
            (r'\bDiscoverist\b', r'<lang xml:lang="en-US">Discoverist</lang>'),
            (r'\bExplorist\b', r'<lang xml:lang="en-US">Explorist</lang>'),
            (r'\bMember\b', r'<lang xml:lang="en-US">Member</lang>'),
            (r'\bVacation Club\b', r'<lang xml:lang="en-US">Vacation Club</lang>'),
            (r'\bHyatt Inclusive Collection\b', r'<lang xml:lang="en-US">Hyatt Inclusive Collection</lang>'),
            (r'\bAlipay\b', r'<lang xml:lang="en-US">Alipay</lang>'),
            (r'\bApple Pay\b', r'<lang xml:lang="en-US">Apple Pay</lang>'),
            (r'\bWeChat Pay\b', r'<lang xml:lang="en-US">WeChat Pay</lang>'),
            (r'(?<!World of )\bHyatt\b(?! Inclusive Collection\b)', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ˈhaɪət">Hyatt</phoneme></lang>'),  # leaves World of Hyatt / Hyatt Inclusive Collection to their own rules
            (r'\bMilestone\b', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="majlstɔn">Milestone</phoneme></lang>'),
            (r'\bMiraval\b', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="miʁaval">Miraval</phoneme></lang>'),
        ]
    },
    "2": {
        "name": "fr-FR",
        "rules": [
                (r'\bWorld of Hyatt\b', r'<lang xml:lang="en-US">World of Hyatt</lang>'),
                (r'\bLifetime\b', r'<lang xml:lang="en-US">Lifetime</lang>'),
                (r'Globalist', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="glɔbalist">Globalist</phoneme></lang>'),
                (r'Discoverist', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="diskɔvøʁist">Discoverist</phoneme></lang>'),
                (r'Explorist', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ɛksplɔʁist">Explorist</phoneme></lang>'),
                (r'\bMember\b', r'<lang xml:lang="en-US">Member</lang>'),
                (r'(?<!World of )Hyatt(?! Inclusive Collection)', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="ˈhaɪət">Hyatt</phoneme></lang>'),  # leaves World of Hyatt / Hyatt Inclusive Collection to their own rules
                (r'\bVacation Club\b', r'<lang xml:lang="en-US">Vacation Club</lang>'),
                (r'Milestone', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="majlstɔn">Milestone</phoneme></lang>'),
                (r'Miraval', r'<lang xml:lang="en-US"><phoneme alphabet="ipa" ph="miʁaval">Miraval</phoneme></lang>'),
                (r'\bHyatt Inclusive Collection\b', r'<lang xml:lang="en-US">Hyatt Inclusive Collection</lang>'),
                (r'\bAlipay\b', r'<lang xml:lang="en-US">Alipay</lang>'),
                (r'\bApple Pay\b', r'<lang xml:lang="en-US">Apple Pay</lang>'),
                (r'\bWeChat Pay\b', r'<lang xml:lang="en-US">WeChat Pay</lang>'),
                (r'\bCourtesy Card\b', r'<lang xml:lang="en-US">Courtesy Card</lang>'),
                (r'\bclientes\b', r'<phoneme alphabet="ipa" ph="kli.jɑ̃t">clientes</phoneme>'),
                (r"\bQu['’]allez-vous\b", r'<phoneme alphabet="ipa" ph="kalevu">Qu’allez-vous</phoneme>'),
                (r'\bDevon\b', r'<phoneme alphabet="ipa" ph="devɔn">Devon</phoneme>'),
                (r'\b(en savoir) plus\b', r'\1 <phoneme alphabet="ipa" ph="ˈplys">plus</phoneme>'),
                (r"(?<!plus )\b(en|de|ou|et) plus\b(?=\s*[,.;:!?]|\s+d(?:es?\b|u\b|['’]))", r'\1 <phoneme alphabet="ipa" ph="ˈplys">plus</phoneme>'),  # only before punctuation or de/des/du/d’; skips "de plus en plus"
        ]
    },
    "3": {
        "name": "ja-JP",
        "rules": [
            (r'(?<![A-Za-z0-9])Avis(?![A-Za-z0-9])', r'<phoneme alphabet="sapi" ph="エイビス">Avis</phoneme>'),  # \b fails next to kana/kanji
        ]
    },
    "4": {
        "name": "zh-CN",
        "rules": [
            (r'(?<![A-Za-z0-9])Hyatt Vacation Club(?![A-Za-z0-9])', r'<lang xml:lang="en-US">Hyatt Vacation Club</lang>'),  # \b fails next to Chinese characters
            (r'(?<![A-Za-z0-9])Miraval(?![A-Za-z0-9])', r'<lang xml:lang="en-US">Miraval</lang>'),
            (r'(?<![A-Za-z0-9])Apple Pay(?![A-Za-z0-9])', r'<lang xml:lang="en-US">Apple Pay</lang>'),
            (r'(?<![A-Za-z0-9])Hyatt Studios(?![A-Za-z0-9])', r'<lang xml:lang="en-US">Hyatt <phoneme alphabet="ipa" ph="ˈstjuːdioʊs">Studios</phoneme></lang>'),
        ]
    },
}
