# Evaluation transcripts (Hindi) ✅

## Successful interaction
User: "मुझे नहीं पता मैं किस योजना के लिए योग्य हूँ।"
Agent: "कृपया अपनी उम्र, वार्षिक आय और रोजगार की स्थिति बताइए।"
User: "उम्र 32, आय 25000, बेरोजगार।"
Agent: "मुझे 1 उपयुक्त योजना मिली: गरीबी उन्मूलन सहायता। क्या मैं आपके लिए आवेदन कर दूँ?"
User: "हाँ"
Agent: "आपका आवेदन सफलतापूर्वक सबमिट कर दिया गया है।"

## Failure (STT noise)
User mumbled -> STT confidence low
Agent: "माफ़ कीजिए, मैं नहीं समझ पाया, क्या आप दोहरा सकते हैं?"

## Edge case (contradictions)
User earlier said वे "बेरोजगार"; later says "मैं खेती करता हूँ, थोड़े बहुत कमाता हूँ"
Agent detects contradiction, asks clarifying question and updates memory.

