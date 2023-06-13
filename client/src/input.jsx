import React, { useState } from 'react';
import './App.css'

function Input(props) {

  const [msg, setMsg] = useState('');

  const handleKeyPress = (event) => 
  {
    if ((event.key === 'Enter' || event.key === undefined) && !event.shiftKey && msg.replace(/\s/g, "").length !== 0) 
    {
      props.onMessage(msg, false);
      setMsg('');
    } 
    else 
    {
      console.log('test')
      event.target.style.height = 'auto';
      event.target.style.height = `${event.target.scrollHeight}px`;
    }
  }

  return (
    <div className="wrapperwrapper">
      <div className="wrapper">
        <textarea type="text" id="textInput" value={msg} onChange={(e) => setMsg(e.target.value)} onKeyDown={handleKeyPress}></textarea>
        <button className="enter" onClick={handleKeyPress}><i className="fa-solid fa-arrow-right"></i></button>
      </div>
    </div>
  )
}

export default Input
