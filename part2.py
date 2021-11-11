"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  diamond = ""
  for i in range(1, size+1):
    diamond += (" " * (size - i) + "*")
    diamond += (" " * (2*i - 3))
    if i >= 2: diamond += "*"
    diamond += "\n"
  for i in range(1, size):
    diamond += (" " * (i) + "*")
    diamond += (" " * ((2 * (size - i) - 3)))
    if i < size-1: diamond += "*"
    diamond += "\n"
  return diamond