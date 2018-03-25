# Find the longest substring with k unique characters in a given string
# Given a string you need to print longest possible substring that has exactly M unique characters. If there are more than one substring of longest possible length, then print any one of them.

# Examples:

# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.

# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.

# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with length 6.

# "aaabbb", k = 3
# There are only two unique characters, thus show error message. 

class Solution:
    def getUnique(self, input_str, number_of_unique_char):
        substring_list = list()
        unique_char_counter = 0


        for char in input_str:
            print('char is : ', char)
            if unique_char_counter == number_of_unique_char:
                if substring_list[-1] == char:
                    substring_list.append(char)
                else: 
                    return substring_list


            if unique_char_counter < number_of_unique_char:

                if not substring_list:
                    print('appending %s to empty substring_list %s, while increasing counter by 1' %(char, substring_list))
                    substring_list.append(char)
                    unique_char_counter = unique_char_counter + 1

                elif substring_list[-1] != char:
                    print('appending %s to %s while increasing counter by 1' %(char, substring_list))
                    unique_char_counter = unique_char_counter + 1
                    substring_list.append(char)

                elif substring_list[-1] == char:
                    print('appending %s to %s without increasing counter' %(char, substring_list))
                    substring_list.append(char)



        return substring_list
        #check if unique char counter is equal to number_of_unique_char

            #if equal, return list

            #if lesser, then add char to list
                #if inserted char is equal to previously_last_char in list, don't increase unique_char_counter

                #else, increase unique char counter

    def kUnique(self, input_string, number_of_unique_char):



        #set unique char counter to 0

        #create list to hold substring

        unique_substr_perm_list = list()

        #iterate through input string,
        for i in range(0, len(input_string)):
            print('input_string[%s:] is : %s' %(i, input_string[i:]))
            result = self.getUnique(str(input_string[i:]), 
                                        number_of_unique_char)
            # unique_substr_perm_list.append()
            

            print('unique_substr_perm_list is : ', result)



if __name__ == '__main__':
    solx = Solution()

    solx.kUnique('aabbcc', 2)
