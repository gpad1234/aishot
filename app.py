from flask import Flask,request, render_template
from openai import OpenAI

import config
import os
os.environ["OPENAI_API_KEY"] = config.API_KEY

#OpenAI.api_key = config.API_KEY
app = Flask(__name__)
client = OpenAI()

@app.get('/home/<menu>')
def single_converter(menu):

    return "You tried accessing 'single_converter' \
    endpoint with value of 'menu' as " + str(menu)


@app.get('/aihome')
def single_aiconverter():
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
  )
  answer=completion.choices[0].message
  print(answer)
  return str(answer)

@app.route("/bot")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #model="gpt-3.5-turbo",
    #messages=[
    #   {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #   {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    #  ]
    #)
    #print(completion.choices[0].message)

@app.route("/get1")
def get_bot_response2():
    userText = request.args.get('msg')
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
    ) 

    answer = response["choices"][0]["text"]
    return str(answer)

@app.route("/get")
def get_bot_response():
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
  )
  answer=completion.choices[0].message
  print(answer)
  return str(answer)







