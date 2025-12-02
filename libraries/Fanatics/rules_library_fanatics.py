rule_sets = {
    "1": {
        "name": "general",
        "rules": [
            (r'\bFanatics Betting and Gaming\b', r'<lang xml:lang="en-US">Fanatics Betting and Gaming</lang>'),
            (r'\bCorporate and Platform Services\b', r'<lang xml:lang="en-US">Corporate and Platform Services</lang>'),
            (r'\bFanatics Collectibles\b', r'<lang xml:lang="en-US">Fanatics Collectibles</lang>'),
            (r'\bMake-A-Wish America\b', r'<lang xml:lang="en-US">Make-A-Wish America</lang>'),
            (r'\bFanatics Corporate\b', r'<lang xml:lang="en-US">Fanatics Corporate</lang>'),
            (r'\bFanatics Commerce\b', r'<lang xml:lang="en-US">Fanatics Commerce</lang>'),
            (r'\bFanatics Foundation\b', r'<lang xml:lang="en-US">Fanatics Foundation</lang>'),
            (r'\bFanatics Events\b', r'<lang xml:lang="en-US">Fanatics Events</lang>'),
            (r'\bStarting Lineup\b', r'<lang xml:lang="en-US">Starting Lineup</lang>'),
            (r'\bFanatics Fest\b', r'<lang xml:lang="en-US">Fanatics Fest</lang>'),
            (r'\bFanatics Collect\b', r'<lang xml:lang="en-US">Fanatics Collect</lang>'),
            (r'\bStar Wars\b', r'<lang xml:lang="en-US">Star Wars</lang>'),
            (r'\bMLB Debut\b', r'<lang xml:lang="en-US">MLB Debut</lang>'),
            (r'\bMVP Buyback\b', r'<lang xml:lang="en-US">MVP Buyback</lang>'),
            (r'\bAll Access\b', r'<lang xml:lang="en-US">All Access</lang>'),

            # Terms that need negative lookahead to prevent partial matches
            (r'\bCorporate\b(?!\s+and\s+Platform\s+Services)', r'<lang xml:lang="en-US">Corporate</lang>'),
            (r'\bCollectibles\b(?!\s*</)', r'<lang xml:lang="en-US">Collectibles</lang>'),
            (r'\bMLB\b(?!\s+Debut)', r'<lang xml:lang="en-US">MLB</lang>'),

            # Remaining single-word terms
            (r'\bJacksonville\b', r'<lang xml:lang="en-US">Jacksonville</lang>'),
            (r'\bManchester\b', r'<lang xml:lang="en-US">Manchester</lang>'),
            (r'\bMichael Rubin\b', r'<lang xml:lang="en-US">Michael Rubin</lang>'),
            (r'\bSportsbook\b', r'<lang xml:lang="en-US">Sportsbook</lang>'),
            (r'\biGaming\b', r'<lang xml:lang="en-US">iGaming</lang>'),
            (r'\bESPN\b', r'<lang xml:lang="en-US">ESPN</lang>'),
            (r'\bMarvel\b', r'<lang xml:lang="en-US">Marvel</lang>'),
            (r'\bNBA\b', r'<lang xml:lang="en-US">NBA</lang>'),
            (r'\bNFL\b', r'<lang xml:lang="en-US">NFL</lang>'),
            (r'\bPWCC\b', r'<lang xml:lang="en-US">PWCC</lang>'),
            (r'\bTopps\b', r'<lang xml:lang="en-US">Topps</lang>'),
            (r'\bWWE\b', r'<lang xml:lang="en-US">WWE</lang>'),
            (r'\bFanCash\b', r'<lang xml:lang="en-US">Fan Cash</lang>'),
            (r'\bfandom\b', r'<lang xml:lang="en-US">fandom</lang>'),
        ]
    },
    "2": {
        "name": "Filipino",
        "rules": [
            (r'\bGaming\b', r'<phoneme alphabet="ipa" ph="ˈɡeiming">Gaming</phoneme>'),
            (r'\biGaming\b', r'<phoneme alphabet="ipa" ph="ˈaiɡeiming">iGaming</phoneme>'),
            (r'\blive\b', r'<phoneme alphabet="ipa" ph="ˈlaiv">live</phoneme>'),
            (r'\bkitain\b', r'<phoneme alphabet="ipa" ph="kitˈain">kitain</phoneme>'),
        ]
    }
}
