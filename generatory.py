import streamlit as st
import openai

openai.api_key = "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"

st.title('Создание новой продуктовой карточки')

def createImageWithGPT(prompt):
  completion = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
  )
  return completion.data[0].url

def generateExplanationText(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1
    )
    return completion.choices[0].text

 
image_url = createImageWithGPT("Кроссовки белые женские спортивные 1 штука")
image_prompt = "Кроссовки белые женские спортивные JOYCITY"

description = generateExplanationText(image_prompt)

col1, col2 = st.columns(2)

col1.write("Проведённая аналитика показала, что параметрами влияющими на продажи являются наименование, бренд, цена, отзывы  и пол(мужская/женская обувь).")

if col1.button("Сгенерировать продуктовую карточку"):
    col2.image(image_url)
    col2.write(description)
else:
    col2.write('Здесь будет карточка')
