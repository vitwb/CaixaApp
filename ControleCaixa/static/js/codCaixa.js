document.getElementById("NovaCaixa").onclick = function autoFill() {
    console.log(generatePassword(4));
    document.getElementById("nomecaixa").value = generatePassword(4) ;
  
  }
  function generatePassword(id) {
    var length = id,
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
    retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
    }