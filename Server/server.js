import express from 'express'
import cors from 'cors'
import { config } from "dotenv"
config()

import { Configuration, OpenAIApi } from "openai"

const openAi = new OpenAIApi(
  new Configuration({
    apiKey: process.env.API_KEY,
  })
)

const app = express();
app.use(cors());
app.use(express.json());
const port = 5000;

app.get('/', (req, res)=> {
  res.send('EssAI Sensei Server');
})

app.listen(port, () => console.log("i hope this works"))

app.post('/', async (req, res) => {

  const requestData = req.body;

  const response = await openAi.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [
      { role: "system", content: "You're the AI behind a chess website called Chess Sensei. Chess Sensei is an AI powered chess coach, analyzig users games and explaing why the best move is the best move. Some times you'll be provided with the users move, the best move, and the best move sequences after the best move has been played, other times you'll be given the entire game along with the mistakes made within the game. You may also be asked questions directly from the user."},
      { role: "user", content: requestData.message},
    ],
  })

  res.status(200).send({
    bot: response.data.choices[0].message.content
  })
});