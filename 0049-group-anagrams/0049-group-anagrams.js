/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
    let data = {}
    
    for (let i =0 ; i < strs.length ; i++){
        
        let key = strs[i].split('').sort().join('')
        
        if (key in data){
            data[key] = [...data[key],strs[i]]
        }
        else{
            data[key] = [strs[i]]
            
        }
        
        
    }
    
    console.log( Object.values(data) )
    
    return Object.values(data)

};