document.addEventListener('DOMContentLoaded', function() {
  const webSocketBridge = new channels.WebSocketBridge();

  webSocketBridge.connect('/ws/');
  webSocketBridge.listen(function(action, stream) {
    var options="";
    for(var i=1;i<5;i++){
      options+="<input id='"+i+"' type='radio' name='chosenoption' value='"+action.options[i-1]+"'><label for='"+i+"'>"+action.options[i-1]+"</label><br>";
    }
    options+="<input type='submit' value='Submit'>"
    document.getElementById('question').innerHTML+=options;
    document.getElementById('question').style.display='block';
  })
  document.ws = webSocketBridge; /* for debugging */
})

function submitted() {
  document.getElementById('question').style.display='none';
}
