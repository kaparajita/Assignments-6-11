class palindrome:
   def __init__(self,inputstr):
         self.inputstr =inputstr
       
   def ispalindrome(self):
        revStr = self.inputstr[::-1]        
        if(revStr == self.inputstr):
            return True
        else:
            return False