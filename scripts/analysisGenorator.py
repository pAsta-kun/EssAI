import openai
import pandas as pd
import time

openai.organization = "org-2MbGT6ap2SgUov1kTz7A5RLp"
openai.api_key = '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'
openai.Model.list()

df = pd.read_csv('/content/drive/MyDrive/EssAITrainingData.csv')
count = 0

first_column = df.iloc[:, 0]
first_column_list = first_column.tolist()

# try:
#     print(str(first_column_list[0]))
# except UnicodeEncodeError:
#     print(str(first_column_list[0]).encode('utf-8'))

for index, texts in enumerate(first_column_list):

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": '''
        As a seasoned undergraduate admissions counselor in the United States, your expertise lies in fine-tuning personal essays, transforming them into compelling narratives that enhance a student's college application. Your reputation for providing incisive, direct feedback, and making any essay unforgettable, sets you apart. High school students turn to you to craft their personal statements in a manner that resonates deeply with top-tier admissions officers.

    Your task is to guide a student towards presenting a personal statement that becomes a beacon within their application, something the admissions team will recall long after the admissions cycle has ended. Your modus operandi involves rigorous, sometimes brutally frank feedback, as you believe in doing whatever it takes to realize a student's dream college admission.

    Given a personal statement essay, provide a comprehensive critique. Rate the essay on a scale of 0 to 100, commenting extensively on its strengths and weaknesses. Your feedback should reflect what was done well, areas of concern, and concrete suggestions for improvement. Embrace your role as the unflinching critic - don't hold back on the truth, no matter how harsh it may seem.

    Essay:''' + texts}
    ]
    )
    count += 1
    df.iloc[index, 1] = completion.choices[0].message['content']
    print("COUNT:")
    print(count)
    print(completion.choices[0].message)
    time.sleep(20)

df.to_csv(r'/content/drive/MyDrive/EssAITrainingData.csv', index=False)
