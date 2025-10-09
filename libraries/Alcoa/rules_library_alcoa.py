rule_sets = {
    "1": {
        "name": "es-es",
        "rules": [
            (r'\bBring Your Own Device\b', r'<lang xml:lang="en-US">Bring Your Own Device</lang>'),
            (r'\bBYOD\b', r'<lang xml:lang="en-US"><say-as interpret-as="characters">BYOD</say-as></lang>'),
        ]
    },
    "2": {
        "name": "fr-ca",
        "rules": [
                (r'\bd’Alcoa\b', r'<phoneme alphabet="ipa" ph="dalkˈoɑ">d’Alcoa</phoneme>'),
                (r'\bAlcoa\b', r'<phoneme alphabet="ipa" ph="alkˈoɑ">Alcoa</phoneme>'),
        ]
    },
    "3": {
        "name": "hu-hu",
        "rules": [
            (r'\bAlcoát\b', r'<phoneme alphabet="ipa" ph="ɒlkoaːt">Alcoát</phoneme>'),
            (r'\bkötelezettségei\b', r'<phoneme alphabet="ipa" ph="køtɛlɛzɛtʃeːgɛi">kötelezettségei</phoneme>'),
            (r'\bkitettség\b', r'<phoneme alphabet="ipa" ph="kitɛtʃeːg">kitettség</phoneme>'),
            (r'\bGenAI\b', r'<phoneme alphabet="ipa" ph="d͡ʒɛn">Gen</phoneme><phoneme alphabet="ipa" ph="ˌɛiˈai">AI</phoneme>'),
            (r'\bCopilot\b', r'<phoneme alphabet="ipa" ph="ˈkoʊpaɪlət">Copilot</phoneme>'),
            (r'\bEdge\b', r'<phoneme alphabet="ipa" ph="ɛd͡ʒ">Edge</phoneme>'),
            (r'\bChatGPT\b', r'<phoneme alphabet="ipa" ph="t͡ʃæt">Chat</phoneme><phoneme alphabet="ipa" ph="ˌd͡ʒiːpiːˈtiː">GPT</phoneme>'),
            (r'\bDeepSeek\b', r'<phoneme alphabet="ipa" ph="diːp">Deep</phoneme><phoneme alphabet="ipa" ph="siːk">Seek</phoneme>'),
            (r'\bAlcoánál\b', r'<phoneme alphabet="ipa" ph="ɒlkoaːnaːl">Alcoánál</phoneme>'),
            (r'\bdesign\b', r'<phoneme alphabet="ipa" ph="dɪˈzaɪn">design</phoneme>'),
            (r'\bITAS\b', r'<phoneme alphabet="ipa" ph="i.ti.ɛi.ɛs">ITAS</phoneme>'),
            (r'\bincidensnek\b', r'<phoneme alphabet="ipa" ph="inʦidɛnʃnɛk">incidensnek</phoneme>'),
            (r'\bAlcoán\b', r'<phoneme alphabet="ipa" ph="ɒlkoaːn">Alcoán</phoneme>'),
            (r'\bBYOD\b', r'<phoneme alphabet="ipa" ph="bi.uai.ou.di">BYOD</phoneme>'),
            (r'\be-mailekhez\b', r'<phoneme alphabet="ipa" ph="iːmeːlɛkhɛz">e-mailekhez</phoneme>'),
            (r'\bincidenst\b', r'<phoneme alphabet="ipa" ph="inʦidɛnʃt">incidenst</phoneme>'),
            (r'\btekintse\b', r'<phoneme alphabet="ipa" ph="tɛkinʧɛ">tekintse</phoneme>'),
        ]
    },
    "4": {
        "name": "pt-br",
        "rules": [
            (r'\bGen-AI\b', r'<lang xml:lang="en-US">Gen-AI</lang>'),
            (r'\bMicrosoft Copilot\b', r'<lang xml:lang="en-US">Microsoft Copilot</lang>'),
            (r'\bChatGPT\b', r'<lang xml:lang="en-US">ChatGPT</lang>'),
            (r'\bDeepSeek\b', r'<lang xml:lang="en-US">DeepSeek</lang>'),
            (r'\bBYOD\b', r'<lang xml:lang="en-US"><say-as interpret-as="characters">BYOD</say-as></lang>'),
            (r'\bviolações\b', r'<phoneme alphabet="ipa" ph="vio.la.sˈõɛs">violações</phoneme>'),
        ]
    },
    "5": {
        "name": "zh-cn",
        "rules": [
            (r'\bMy Alcoa\b', r'<lang xml:lang="en-US">My Alcoa</lang> '),
            (r'\bAlcoa\b', r'<lang xml:lang="en-US">Alcoa</lang>'),
            (r'\bGen-AI\b', r'<lang xml:lang="en-US">Gen-AI</lang>'),
            (r'\bMicrosoft Copilot\b', r'<lang xml:lang="en-US">Microsoft Copilot</lang>'),
            (r'\bChatGPT\b', r'<lang xml:lang="en-US">ChatGPT</lang>'),
            (r'\bDeepSeek\b', r'<lang xml:lang="en-US">DeepSeek</lang>'),
            (r'\bPrivacy by Design\b', r'<lang xml:lang="en-US">Privacy by Design</lang>'),
            (r'\bPbD\b', r'<lang xml:lang="en-US">PbD</lang>'),
            (r'\bBYOD\b', r'<lang xml:lang="en-US"><say-as interpret-as="characters">BYOD</say-as></lang>'),
            (r'\bAndrew\b', r'<lang xml:lang="en-US">Andrew</lang>'),
        ]
    },
}
