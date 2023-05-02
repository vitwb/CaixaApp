


function onScanSuccess(decodedText, decodedResult) {
  // handle the scanned code as you like, for example:
  
  var elem = document.getElementById("reader");
  elem.remove();
  console.log("OSS");
  document.getElementById('resultado').innerHTML=`<a>"${decodedText}"</a>`
  html5QrcodeScanner.clear();
}

function onScanFailure(error) {
    // handle scan failure, usually better to ignore and keep scanning.
    // for example:
    console.warn(`Code scan error = ${error}`);
  }
  

    
document.getElementById("CriarButton").onclick = function(){
  const html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 20, qrbox: {width: 250, height: 250} },
    /* verbose= */ true);
    html5QrcodeScanner.render(onScanSuccess, onScanFailure);
};



