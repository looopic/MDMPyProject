function getSentiment(event, text) {
  if (!text || event.key !== "Enter") {
    answer.innerHTML = '';
    return;
  }
  answerPart.style.visibility = "visible";

  // Get Sentiment
  fetch('/submit?' + new URLSearchParams({
    text: text,
  }), {
    method: 'GET',
    headers: {}
  }).then(
    response => response.blob())
    .then(blob=>{
      var objectURL = URL.createObjectURL(blob);
      var myImage=new Image()
      console.log(objectURL)
      myImage.src = objectURL;
      document.getElementById("answer").append(myImage)
    }
  ).then(
    success => console.log(success)
  ).catch(
    error => console.log(error)
  );
}
