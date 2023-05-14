class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        sign_bit = 0x80000000
        max_val = 0x7FFFFFFF
    
        while b != 0:
            # Calculate the sum without considering the carry
            sum = (a ^ b) & mask
    
            # Calculate the carry, considering sign extension
            carry = ((a & b) << 1) & mask
    
            # Update a and b for the next iteration
            a = sum
            b = carry
    
        # Handle negative overflow
        if a & sign_bit:
            a = -((~a + 1) & max_val)
    
        return a