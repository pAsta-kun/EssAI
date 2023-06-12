import './App.css'

function Input(props) {

  const handleKeyPress = (event) =>
  {
    if (event.key === 'Enter' || event.key === undefined) {
      const msg = document.getElementById('textInput').value;
      document.getElementById('textInput').value = '';
      props.onMessage(msg, false);
    }
  }
  return (
    <div className="wrapper">
      <input type="text" id="textInput" onKeyDown={handleKeyPress}/>
      <button className="enter" onClick={handleKeyPress}><i className="fa-solid fa-arrow-right"></i></button>
    </div>
  )
}

export default Input
