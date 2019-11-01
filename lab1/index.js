const plaintext = ' abcdefghijklmnopqrstuvwxyz';
const cyphertext = plaintext.toUpperCase();
const mod = (x, n) => (x % n + n) % n;
//this mod formula computes the modulo for positive and negative numbers.
//if you have a positive number (x) it does not change the result, adding n and then applying modulo by n
//if you have a negative number, the result won't be the right one, so we add n to obtain a positive number

function getPlainText() {
    //the function gets the original text from the first textbox and returns it, to be crypted
    var text = document.getElementById('text1');
    return (text != null) ? text.value : ''
}

function getCypherText() {
    //the function gets the cypher text from the second textbox and returns it, to be decrypted
    var text = document.getElementById('text2');
    return (text != null) ? text.value : ''
}

function getKey() {
    //the function gets the key from the input
    var key = document.getElementById('key');
    return (key != null) ? parseInt(key.value) : NaN
}

function crypt () {
    //crypts the original text and puts the result in the second textbox
    var text = getPlainText();
    var key = getKey();
    var result = '';

    for (i in text) {
        result += cyphertext[mod((plaintext.indexOf(text[i]) + key), (plaintext.length))];
    }

    document.getElementById('text2').value = result;
    validateInputs();
}

function decrypt() {
    //decrypts the cypher text and puts the result in the first textbox
    var text = getCypherText();
    var key = getKey();
    var result = '';

    for (index in text) {
        result += plaintext[mod((cyphertext.indexOf(text[index]) - key), (cyphertext.length))];
    }

    document.getElementById('text1').value = result;
    validateInputs();
}

function validateInputs() {
    /*checks if the input values are correct : no illegal characters, no missing key allowed
      shows a message if there are any illegalities, and the buttons remain deactivated
      activates the buttons based on the area the text was entered, if no illegality occurred (if there is text in both text boxes, the buttons are deactivated)
     */
    deactivateBtns();

    text1 = getPlainText();
    text2 = getCypherText();
    key = getKey();

    var containsPlainChars = false;
    var containsCypherChars = false;
    var containsIllegalChars = false;

    for (index in text1) {
        if (plaintext.includes(text1[index])) {
            containsPlainChars = true;
        }
        else {
            containsIllegalChars = true;
        }
    }

    for (index in text2) {
        if (cyphertext.includes(text2[index])) {
            containsCypherChars = true;
        }
        else {
            containsIllegalChars = true;
        }
    }

    if (text1 === '' && text2 === '') {
        hideAlert()
    }
    else if (isNaN(key)) {
        setAlert('Key is not set')
    }
    else if (containsIllegalChars) {
        setAlert('Text contains illegal characters!');
    }
    else if (containsPlainChars && containsCypherChars) {
        //setAlert('Do not mix characters!');
    }
    else if (containsPlainChars) {
        hideAlert();
        activateCryptBtn();
    }
    else {
        hideAlert();
        activateDecryptBtn();
    }
}

function deactivateBtns() {
    //deactivates both buttons
    document.getElementById('crypt-btn').disabled = true
    document.getElementById('decrypt-btn').disabled = true
}

function activateCryptBtn() {
    document.getElementById('crypt-btn').disabled = false;
}

function activateDecryptBtn() {
    document.getElementById('decrypt-btn').disabled = false;
}

function setAlert(text) {
    //shows alert message
    document.getElementById('alert').style.display = 'block';
    document.getElementById('alert').innerHTML = text;
}

function hideAlert() {
    document.getElementById('alert').innerHTML = '';
    document.getElementById('alert').style.display = 'none';
}

validateInputs();