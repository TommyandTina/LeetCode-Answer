class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #create a dictionary for same type of brackets, closing bracket go first
        mapping = {")":"(", "}" : "{", "]" : "["}

        for char in s:
            #use values() to get the value from key in dictionary
            if char in mapping.values():
                stack.append(char) #bring the open bracket to stack
            else:
                #handle closing bracket here
                #if stack is blank OR stack does not match with the openning bracket type of char -> False
                if not stack or mapping[char] != stack.pop():
                    return False
        #until here, we want to return True. But in some case stack did not pop out all char -> need to check stack
        return not stack