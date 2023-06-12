import React from 'react'
import ReactDOM from 'react-dom/client'
import Input from './input.jsx'
import TextBubble from './messageArea.jsx'
import './index.css'
import { useState } from 'react'


function App()
{
  const [messages, setMessages] = useState([]);

  const handleMessage = (msg, isAi) => {
    setMessages(prevState => [...prevState, {message: msg, isAi: isAi}]);
    handleResponse(msg);
  };
  
  const handleResponse = async (msg) => {
    let response = await getAIResponse(msg);
    //let response = msg;
    setMessages(prevState => [...prevState, {message: response, isAi: true}]);
  }

  return (
    <React.StrictMode>
      <div className="main">
        <h1>EssAI</h1>
        <div className="messageArea">
        {messages.map((msg, index) => (
          <TextBubble key={index} isAI={msg.isAi} text={msg.message}/>
        ))}
        </div>
        <Input onMessage={handleMessage}/>
      </div>
    </React.StrictMode>
  )
  
}

ReactDOM.createRoot(document.getElementById('root')).render(<App/>)

async function getAIResponse(prompt)
    {

      console.log(prompt)
      try {
        //Ai Response stored here
        const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: JSON.stringify({
          message: prompt
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
        }).then((response) => response.json());

        //Getting the AI response in the right format
        const botResponse = response.bot.trim();
        console.log(botResponse);
        return botResponse
      } catch (error) {
        console.log(error);
        return error;
      }
      
    }