


function onScanSuccess(decodedText, decodedResult) {
  // handle the scanned code as you like, for example:
  
 
  document.getElementById('Cod_Caixa').value= decodedText
  document.getElementById("html5-qrcode-button-camera-stop").click();
  reader2();
  document.getElementById("resultado2").click();
}

function onScanFailure(error) {
    // handle scan failure, usually better to ignore and keep scanning.
    // for example:
    console.warn(`Code scan error = ${error}`);
  }
  
  function onScanSuccess2(decodedText, decodedResult) {
    // handle the scanned code as you like, for example:
    
    var elem = document.getElementById("reader2");
    
    
    document.getElementById('Cod_Cliente').value= decodedText
    
    elem.getElementById("html5-qrcode-button-camera-stop").click();
   
  }
  
  function onScanFailure2(error) {
      // handle scan failure, usually better to ignore and keep scanning.
      // for example:
      console.warn(`Code scan error = ${error}`);
    }
    

  window.onload = function reader1 (){   

  const html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 20, qrbox: {width: 250, height: 250} },
    /* verbose= */ true);
    html5QrcodeScanner.render(onScanSuccess, onScanFailure);

}


function reader2(){   

  const html5QrcodeScanner2 = new Html5QrcodeScanner(
    "reader2",
    { fps: 20, qrbox: {width: 250, height: 250} },
    /* verbose= */ true);
    html5QrcodeScanner2.render(onScanSuccess2, onScanFailure2);

}
