/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
    let alphaNum = 'ZXCVBNMASDFGHJKLQWERTYUIOPzxcvbnmasdfghjklqwertyuiop1234567890'
    let k=''
    
    for ( let i=0 ; i<s.length ; i++){
        if(alphaNum.includes(s[i]) ){
            k+= s[i]
        }
        
    }
    
    return k.toLowerCase().split('').reverse().join('') == k.toLowerCase()
    
    console.log(k)
    
};