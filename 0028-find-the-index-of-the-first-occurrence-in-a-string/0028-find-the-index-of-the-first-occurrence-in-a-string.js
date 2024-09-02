/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let lenHay = haystack.length
    let lenNeedle = needle.length
    
    if (lenNeedle===0){
        return 0
    }
    
    for(let i=0 ; i < lenHay-lenNeedle+1 ; i++ ){
        
        if(haystack.substring(i, i+lenNeedle  ) === needle ){
            return i
        }
        
        
        
        
    }
    return -1
    
};

// /**
//  * @param {string} haystack
//  * @param {string} needle
//  * @return {number}
//  */
// var strStr = function(haystack, needle) {
//     let lenHay = haystack.length;
//     let lenNeedle = needle.length;
    
//     if (lenNeedle === 0) {
//         return 0;
//     }
    
//     for (let i = 0; i <= lenHay - lenNeedle; i++) {
//         if (haystack.substring(i, i + lenNeedle) === needle) {
//             return i;
//         }
//     }
    
//     return -1;
// };
