class Solution(object):
    def interpret(self, command):
        strs = ""
        final = ""
        for a in range(0, len(command)):
            strs += command[a]
            if strs == "G":
                final += "G"
                strs = ""
            elif strs == "()":
                final += "o"
                strs = ""
            elif strs == "(al)":
                final += "al"
                strs = ""
        return final
            
                
        