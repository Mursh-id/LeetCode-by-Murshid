/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    
    const error = (message) => { throw new Error(message); }
    
    return {
        toBe: (val1) => {
            return val === val1 ? true : error("Not Equal");
        },
        notToBe: (val2) => {
            return val !== val2 ? true : error("Equal");
        }
    }
};


/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */