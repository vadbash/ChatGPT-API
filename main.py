import openai
import re

API_KEY = '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'
openai.api_key = f'{API_KEY}'

#Function
def analyze(text):
    response = openai.Completion.create(
      engine="davinci",
      prompt=text,
      max_tokens=150,
      temperature=0.5
    )
    #Result
    results = response["choices"][0]["text"]
    w_count = re.findall(r'\b\w+\b', results)
    s_count = re.findall(r'[A-Z][^\.!?]*[\.!?]', results)
    return {
        "w_count": len(w_count),
        "s_count": len(s_count),
    }

with open("text.txt", "r") as file:
    text = file.read()

#Finish result
results = analyze(text)

print("Words count: ", results["w_count"])
print("Sentences count: ", results["s_count"])
