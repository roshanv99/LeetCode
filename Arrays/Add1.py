#Convert list to int and then add 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int()
        size = len(digits)-1
        
        for n in digits:
            num += n * (10**size)
            size -=1
        num +=1
        return (list(map(int,list(str(num)))))
      
      
      
      #OR
      
      
      class Solution(object):
    def plusOne(self, digits):
        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0]
          
          #OR
          
          def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits)-1, -1, -1):
            digits[index] += 1
            if digits[index] != 10:
                return digits
            digits[index] = 0
        return [1] + digits
