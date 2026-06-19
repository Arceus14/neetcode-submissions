import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        alphabets = list(string.ascii_lowercase) 
        dict_alpha = {key : 0 for key in alphabets}
        dict_alpha2 = {key : 0 for key in alphabets}
        
        for i in s:
            dict_alpha[i] += dict_alpha.get(i, 0) + 1
        #print(dict_alpha)

        for i in t:
            dict_alpha2[i] += dict_alpha2.get(i, 0) + 1
        #print(dict_alpha2)

        if dict_alpha == dict_alpha2:
            return True
        else:
            return False



            
