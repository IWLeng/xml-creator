rule_sets = {
    "1": {
        "name": "English",
        "rules": [
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[: ]?\s*711(?!\d))?', lambda m: f'<say-as interpret-as="characters">TTY</say-as>' + (': <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
            (r'\bLead\b(?!\s+(?:to|toward|towards|by|on|a|an|the|you|your|our|their|healthier|healthy|longer|better)\b)', r'<phoneme alphabet="ipa" ph="lɛd">Lead</phoneme>'),
            (r'\bAmeriHealth\b', r'<phoneme alphabet="ipa" ph="ʌmɛɹʌ">Ameri</phoneme>Health'),
            (r'\bCaritas\b', r'<phoneme alphabet="ipa" ph="kæɹ.ətɔs">Caritas</phoneme>'),
            (r'\bColon\b', r'<phoneme alphabet="ipa" ph="ˈkoʊ.lən">Colon</phoneme>'),
            (r'He, Him, His', r'He; Him; His.'),
            (r'She, Her, Hers', r'She; Her; Hers.'),
            (r'They, Them, Theirs', r'They; Them; Theirs.'),
            (r'\bTHSteps\b', r'Texas Health Steps'),
            (r'Star Plus', r'Star-Plus'),
            (r'\bCopay\b', r'Co-pay'),
            (r'\bTanir\b', r'<phoneme alphabet="ipa" ph="tænɪˈiɝ">Tanir</phoneme>'),
            (r'Humana', r'<phoneme alphabet="ipa" ph="hjumɛːnə">Humana</phoneme>'),
            (r'Allwell', r'All-well'),
            (r'Him/her/them', r'him, / her, / them'),
            (r'IV Drugs', r'<say-as interpret-as="characters">IV</say-as> Drugs'),
            (r'tdap', r't-dap'),
            (r'Para español, presione el número 2', r'<phoneme alphabet="ipa" ph="ˈpə.ˌrə">Para</phoneme> <phoneme alphabet="ipa" ph="es.ˌpæ.ni.ˈol">español</phoneme>, <phoneme alphabet="ipa" ph="prɛ.sio.nɛ">presione</phoneme> <phoneme alphabet="ipa" ph="ɛl">el</phoneme> <phoneme alphabet="ipa" ph="ˈnu.mɛɹo">número</phoneme> <phoneme alphabet="ipa" ph="dos">2</phoneme>'),
            (r'Para escuchar esta llamada en español, presione 2', r'<phoneme alphabet="ipa" ph="ˈpə.ˌrə">Para</phoneme> escuchar <phoneme alphabet="ipa" ph="ˈɛs.ˌtə">esta</phoneme> yamada <phoneme alphabet="ipa" ph="ɛn">en</phoneme> <phoneme alphabet="ipa" ph="es.ˌpæ.ni.ˈol">español</phoneme>, <phoneme alphabet="ipa" ph="prɛ.sio.nɛ">presione</phoneme> <phoneme alphabet="ipa" ph="dos">2</phoneme>'),
            (r'Para escuchar este mensaje en español, por favor marque el 2', r'<phoneme alphabet="ipa" ph="ˈpə.ˌrə">Para</phoneme> <phoneme alphabet="ipa" ph="ɛs.ˌku.ˈtʃar">escuchar</phoneme> <phoneme alphabet="ipa" ph="ˈɛs.ˌtɛ">este</phoneme> <phoneme alphabet="ipa" ph="mɛn.ˈsa.he">mensaje</phoneme> <phoneme alphabet="ipa" ph="ɛn">en</phoneme> <phoneme alphabet="ipa" ph="es.ˌpæ.ni.ˈol">español</phoneme>, <phoneme alphabet="ipa" ph="por">por</phoneme> <phoneme alphabet="ipa" ph="fə.ˈvor">favor</phoneme>, márkE <phoneme alphabet="ipa" ph="ɛl">el</phoneme> <phoneme alphabet="ipa" ph="dos">2</phoneme>'),
            (r'avmed', r'AvMed'),
            (r'av med', r'AvMed'),
            (r'well point', r'WellPoint'),
            (r'(?<!\d)(1[-. ]?)?((?:\(\d{3}\)\s?|\d{3}[-. ])\d{3}[-. ]\d{4})(?!\d)', r'<say-as interpret-as="telephone">\1\2</say-as>'),
            (r'My Benefits dot Nations Benefits dot com', r'My Benefits dot Nations Benefits, dot com')
        ]
    },
    "2": {
        "name": "Spanish",
        "rules": [
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[: ]?\s*711(?!\d))?', lambda m: f'<say-as interpret-as="characters">TTY</say-as>' + (', <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
            (r'To continue this call in English, press one', r'To <phoneme alphabet="ipa" ph="kənˈtɪnjuː">continue</phoneme> this call in English, press one'),
            (r'To continue this call in English, press 1', r'To <phoneme alphabet="ipa" ph="kənˈtɪnjuː">continue</phoneme> this call in English, press one.'),
            (r'AvMed', r'Av-Med'),
            (r'avmed', r'Av-Med'),
            (r'\bav med\b', r'Av-Med'),
            (r'Healthyperks', r'Healthy-perks'),
            (r'Card\.', r'<phoneme alphabet="ipa" ph="kɑɹd">Card</phoneme>.'),
            (r'\belle\b', r'<phoneme alphabet="ipa" ph="eʎe">elle</phoneme>'),
            (r'\bgenderqueer\b', r'<phoneme alphabet="ipa" ph="ˈd͡ʒɛndɚ">gender</phoneme><phoneme alphabet="ipa" ph="kwɪɹ">queer</phoneme>'),
            (r'Aloha Care', r'<phoneme alphabet="ipa" ph="əˈloʊˌhɑ">Aloha</phoneme>-Care'),
            (r'\bJersey\b', r'<phoneme alphabet="ipa" ph="ˈd͡ʒɝzi">Jersey</phoneme>'),
            (r'Wellpoint', r'Well-point'),
            (r'well point', r'Well-point'),
            (r'AmeriHealth', r'<phoneme alphabet="ipa" ph="amɛɹʌ">Ameri</phoneme>-Health'),
            (r'Caritas', r'<phoneme alphabet="ipa" ph="ˈkæɹiˌtʌsː">Caritas</phoneme>'),
            (r'\bWellCare\b', r'Well-Care'),
            (r'\bAllWell\b', r'All-Well'),
            (r'\bRightCare\b', r'Right-Care'),
            (r'\bTexas\b', r'<phoneme alphabet="ipa" ph="ˈtɛk.səs">Texas</phoneme>'),
            (r'\bFirstCare\b', r'First-Care'),
            (r'\bPlans\b', r'<phoneme alphabet="ipa" ph="plænz">Plans</phoneme>'),
            (r'\bPlus\b', r'Plas'),
            (r'\bChoice\b', r'Chois'),
            (r'\bDiverge\b', r'<phoneme alphabet="ipa" ph="daɪˈvɝd͡ʒ">Diverge</phoneme>'),
            (r'\bPCP\b', r'<phoneme alphabet="ipa" ph="piːsiːpiː">PCP</phoneme>'),
            (r'\bNordyke\b', r'<phoneme alphabet="ipa" ph="ˈnor.daik">Nordyke</phoneme>'),
            (r'\bTanir\b', r'Taníier'),
            (r'\bMy Family Doctor\b', r'My Family <phoneme alphabet="ipa" ph="ˈdɔktɚ">Doctor</phoneme>'),
            (r'Capital Blue', r'Cápital Blue'),
            (r'(?-i:\bHumana\b)', r'<phoneme alphabet="ipa" ph="hjuˈmɛna">Humana</phoneme>'),  # (?-i:...) = case-sensitive, so the Spanish adjective humana is left alone
            (r'\bMedica\b', r'Médica'),
            (r'\bla 1\b', r'la una'),
            (r'\bAdvantage MD\b', r'Advantage <phoneme alphabet="ipa" ph="ɛm">M</phoneme><phoneme alphabet="ipa" ph="diː">D</phoneme>'),
            (r'(?<!\d)(1[-. ]?)?((?:\(\d{3}\)\s?|\d{3}[-. ])\d{3}[-. ]\d{4})(?!\d)', r'<say-as interpret-as="telephone">\1\2</say-as>'),
            (r'\bCentene\b', r'Centín'),
            (r'a través', r'através'),
            (r'Flexible Benefit', r'<phoneme alphabet="ipa" ph="ˈflɛk.sɪ.bəl">Flexible</phoneme> Benefit'),
            (r'\b1 Mes\b', r'un mes'),
            (r'My Benefits punto Nations Benefits punto com', r'My Benefits, punto, Nations Benefits, punto com'),
            (r'\bcolon\b', r'cólon'),
            (r'\bDual Care\b', r'Dúal Care'),
            (r'\bHealthPlan\b', r'Health-Plan'),
            (r'\bIntake\b', r'ínteik'),
            (r'\bcure\b', r'cúre'),
        ]
    },
    "3": {
        "name": "Korean",
        "rules": [
            (r'(?<![A-Za-z])Centene(?![A-Za-z])', r'<lang xml:lang="en-US">Centene</lang>'),  # not \b: a Korean particle can follow directly (Centene의)
            (r'(?<![\d에-])(?<![에일주월년연달] )(?<!하루 |마다 )([0-9])번(?!\s*(?:째|씩|이상|이하|정도|더|만))', r'<say-as interpret-as="number_digit">\1</say-as>번'),  # skips counts (하루에 2번, 매일 2번, 2번째, 3번씩) and the last digit of a longer number (711번)
            (r'10자리', r'<phoneme alphabet="ipa" ph="jʌl">10</phoneme>자리'),
            (r'(?<![가-힣])회의', r'<phoneme alphabet="ipa" ph="ˈhø̞ːi">회의</phoneme>'),
            (r'24시간', r'<say-as interpret-as="cardinal">24</say-as>시간'),
            (r'(?<!\d)(?:(\d)[-. ]?)?\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})(?!\d)', lambda m: f'<say-as interpret-as="characters">{m.group(1)}</say-as>-<say-as interpret-as="characters">{m.group(2)}</say-as>-<say-as interpret-as="characters">{m.group(3)}</say-as>-<say-as interpret-as="characters">{m.group(4)}</say-as>' if m.group(1) else f'<say-as interpret-as="characters">{m.group(2)}</say-as>-<say-as interpret-as="characters">{m.group(3)}</say-as>-<say-as interpret-as="characters">{m.group(4)}</say-as>'),
            (r'(?<![A-Za-z])(Wellcare(?: By (?:Delaware First Health|Superior HealthPlan|Allwell|Fidelis Care))?)(?![A-Za-z])', r'<lang xml:lang="en-US">\1</lang>'),  # not \b: a Korean particle can follow directly (Wellcare에)
        ]
    },
    "4": {
        "name": "Vietnamese",
        "rules": [
            (r'\bCentene\b', r'<lang xml:lang="en-US">Centene</lang>'),
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[: ]?\s*711(?!\d))?', lambda m: f'TTY' + (': <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
            (r'(?<!\d)(?:(1)[-. ]?)?\(?(\d{3})\)?[-. ]?(\d{3})[-. ](\d{4})(?!\d)',  lambda m: (f'<say-as interpret-as="characters">{m.group(1)}</say-as>-' if m.group(1) else '') +            f'<say-as interpret-as="characters">{m.group(2)}</say-as>-<say-as interpret-as="characters">{m.group(3)}</say-as>-<say-as interpret-as="characters">{m.group(4)}</say-as>'),
            (r'\b(Wellcare(?: By (?:Delaware First Health|Superior HealthPlan|Allwell|Fidelis Care))?)\b', r'<lang xml:lang="en-US">\1</lang>'),
        ]
    },
    "5": {
        "name": "Chinese (Simplified)",
        "rules": [
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[:： ]?\s*711(?!\d))?', lambda m: f'<say-as interpret-as="characters">TTY</say-as>' + (': <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
            (r'(?<![A-Za-z])(Wellcare(?: By (?:Delaware First Health|Superior HealthPlan|Allwell|Fidelis Care))?)(?![A-Za-z])', r'<lang xml:lang="en-US">\1</lang>'),  # not \b: Chinese puts no space around it (致电Wellcare。)
        ]
    },
    "6": {
        "name": "Armenian",
        "rules": [
            (r'\bKaiser Permanente\b', r'<lang xml:lang="en-US">Kaiser Permanente</lang>'),
            (r'\bID\b', r'<lang xml:lang="en-US">ID</lang>'),
            (r'(?<!w3\.)\borg\b', r'<lang xml:lang="en-US">org</lang>'),  # (?<!w3\.) keeps it off the www.w3.org URLs in the <speak> header
            (r'\b(Wellcare(?: By (?:Delaware First Health|Superior HealthPlan|Allwell|Fidelis Care))?)\b', r'<lang xml:lang="en-US">\1</lang>'),
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[: ]?\s*711(?!\d))?', lambda m: f'<lang xml:lang="en-US"><say-as interpret-as="characters">TTY</say-as></lang>' + (': <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
        ]
    },
    "7": {
        "name": "Russian",
        "rules": [
            (r'\b(Wellcare(?: By (?:Delaware First Health|Superior HealthPlan|Allwell|Fidelis Care))?)\b', r'<lang xml:lang="en-US">\1</lang>'),
            (r'(?<![A-Za-z])TTY(?![A-Za-z])(?:[: ]?\s*711(?!\d))?', lambda m: f'<say-as interpret-as="characters">TTY</say-as>' + (': <say-as interpret-as="characters">711</say-as>' if '711' in m.group() else '')),
            (r'(?<!\d)(1[-. ]?)?((?:\(\d{3}\)\s?|\d{3}[-. ])\d{3}[-. ]\d{4})(?!\d)', r'<say-as interpret-as="telephone">\1\2</say-as>'),
        ]
    }
    
}