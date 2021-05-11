document.addEventListener('DOMContentLoaded', function() {
    const webSocketBridge = new channels.WebSocketBridge();
    webSocketBridge.connect('/ws/');
    webSocketBridge.listen(function(action, stream) {
      if(action.type=="start"){
        $('#what').text(action.qn);
        $('#question').text("Question "+action.qno);
        $(".content").slideToggle();
        for(var i=0;i<4;i++){
          $('#flexRadioDefault'+i).val(action.options[i]);
          $('#label'+i).html(action.options[i]);
        }
        setTimeout(function (){
          submit();
          $(".content").slideToggle();
        },5000);
      }else{
        alert("You scored "+$("#score").text());
      }
    }
  )
    document.ws = webSocketBridge; /* for debugging */
  });
  
  function submit() {
    $.ajax({
      type:"POST",
      url:"http://127.0.0.1:8000/student",
      data:  {
        course : $("[name='course']").val(),
        qno    : $("#question").text().split(" ")[1],
        chosenoption : $("[name='chosenoption']:checked").val() 
        },
      success: function(data){
        if(data!="wrong"){
          $("#score").text(data);
        }
      }
    });
  }