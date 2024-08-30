/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
    let valuesObj = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000,
    }
    
    let symbolArray = s.split('')
    
    let number = 0
    console.log(number)
    
    
    
    for( let i =0 ; i < s.length ; i++ ){
        if( i !== s.length-1 &&  valuesObj[symbolArray[i]] < valuesObj[symbolArray[i+1]] ){
            number = number - valuesObj[symbolArray[i]]
            
            
        }else{
            console.log(symbolArray)
            number = number + valuesObj[symbolArray[i]]
            
        }
    }
    
    return number
    
    
    
    
};