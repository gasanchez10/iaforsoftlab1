import requests
import json
import google.generativeai as genai
import os

model = genai.GenerativeModel('gemini-1.5-flash')

# JSON file
f = open ('config.json', "r")
data = json.loads(f.read())
genai.configure(api_key=data["GOOGLE_API_KEY"])

# Example usage
few_shot_prompt ="A whatpu is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:We were traveling in Africa and we saw these very cute whatpus.To do a farduddle means to jump up and down really fast. An example of a sentence that uses the word farduddle is:"
prompt_chain = "The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1. A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False. The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.  A:"
knowledge_prompt = "Part of golf is trying to get a higher point total than others. Yes or No?"

promts=[few_shot_prompt, prompt_chain, knowledge_prompt]
responses=[]
for i in promts:
    response = model.generate_content(i)
    responses.append(response.text)


# Specify the file name
file_name = "output.txt"

# Open the file in write mode and write each element of the array to the file
with open(file_name, 'w') as file:
    for line in responses:
        file.write(line + "\n")

print(f"Data successfully written to {file_name}")