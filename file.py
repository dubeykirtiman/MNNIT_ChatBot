import openai
openai.api_key='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'
prompt=input("please write the query ")
while(prompt!='q'):
        completions=openai.Completion.create(engine='text-davinci-002',prompt=prompt,max_tokens=1024)
        message=completions.choices[0].text
        print(message)
        prompt=input("your input ")
