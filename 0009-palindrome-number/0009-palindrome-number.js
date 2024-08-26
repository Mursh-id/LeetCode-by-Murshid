/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    let str = x.toString()
    console.log(x)
    
    let reversedStr = str.split("").reverse().join("")
     console.log(reversedStr)
    
    if( str === reversedStr){
        return true
    }
    return false
};