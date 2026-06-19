import string, json
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabets = list(string.ascii_lowercase) 
        dict_alpha ={ word : {key : 0 for key in alphabets} for word in strs}


        for word in strs:
            for each in word:

                dict_alpha[word][each] +=  1
        #print(dict_alpha)
        dict_list = []
        for word in dict_alpha:
            dict_list.append(str(dict_alpha[word]))

        dict_list = list(set(dict_list))
        final_list = []
        for each in dict_list:
            sub_list = []
            for word in strs:
                if str(dict_alpha[word]) == each:
                    sub_list.append(word)
            final_list.append(list(sub_list))

        
        return final_list