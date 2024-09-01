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
    
    
    let number = 0
    
    
    
    for( let i =0 ; i < s.length ; i++ ){
        if( i !== s.length-1 &&  valuesObj[s[i]] < valuesObj[s[i+1]] ){
            number = number - valuesObj[s[i]] + valuesObj[s[i+1]]
            
            i++
            
            
        }else{
            console.log(s)
            number = number + valuesObj[s[i]]
            
        }
    }
    
    return number
    
    
    
    
};