/**
 * @param {string[]} strs - Array of strings to group into anagrams
 * @return {string[][]} - Array of arrays, where each sub-array contains anagrams
 */
var groupAnagrams = function(strs) {
    
    // Initialize an empty object to store grouped anagrams
    let data = {};
    
    // Iterate over each string in the input array
    for (let i = 0; i < strs.length; i++) {
        
        // Sort the characters of the current string to create a key
        // This ensures all anagrams have the same key
        let key = strs[i].split('').sort().join('');
        
        // If the key already exists in the data object,
        // append the current string to the corresponding array
        if (key in data) {
            data[key] = [...data[key], strs[i]];
        } else {
            // If the key doesn't exist, create a new key-value pair
            // The key is the sorted string, and the value is an array containing the current string
            data[key] = [strs[i]];
        }
    }
    
    // Log the values of the data object to see the grouped anagrams
    console.log(Object.values(data));
    
    // Return the values of the data object, which are arrays of anagrams
    return Object.values(data);
};
