'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 Notice
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.



Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
'''



class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        #sL = s.lower()
        length = len(s)
        if length < 2:
            return True
        start  =0; end = length -1;

        while start < end:
            strStart = s[start].lower(); strEnd = s[end].lower();
            if self.isAlphanumeric(strStart) == False:
                start += 1 
                #print( "strstart1 is ", strStart)
                continue;
            #print( "strstart2 is ", strStart)
            if self.isAlphanumeric(strEnd) == False:
                end -= 1 ;
                continue;
            print("start and end is ", start, end)
            print("strStart and strEnd", strStart, strEnd)
            if ( strStart == strEnd ):
                start+=1;
                end -= 1;
            else:
                return False;
        print("last start and end",start, end);
        print(s[start],s[end])
        
        if s[start].lower() == s[end].lower():
            return True;
        else:
            return False;
            
    def isAlphanumeric(self, data):
        res = False;
        if ((data <= 'z' and data >= 'a') or (data <= '9' and data >= '0')):            
            res = True;
        else:
            res = False;
        #print("data and res  ",data, res)
        return res;
data = "A man, a plan, a canal: Panama "
data='aa'
print("data is ", data)
mySol = Solution()
res = mySol.isPalindrome(data)
print("res is ",res)