function binaryAgent(str){

    // split str by spaces into an array of binary Agents
    var _binAgents = str.split(" ");

    // get charCode from each binary string
    var _charCodes = [];

    for (var i = 0; i < _binAgents.length; i++){
        _charCodes.push(parseInt(_binAgents[i],2));
    }

    //get letters back from array of charCodes
    var _alphaNums = [];

    for (var j = 0; j < _charCodes.length; j++){
        _alphaNums.push(String.fromCharCode(_charCodes[j]));
    }

    // turn array into string and remove commas
    var sentence = _alphaNums.join('');
    
    console.log(sentence);

    // return the new sentence
    return sentence;
}

binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");


str.split().map(stuff)
