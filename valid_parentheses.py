class Solution:
    def isValid(self, s: str) -> bool:
        rel = []
        for i in range(len(s)):
            if len(rel) == 0 :
                if s[i] in "}])":
                    return 0
                rel.append(s[i])
            if s[i] in "({[":
                rel.append(s[i])
            elif s[i] == ")" and rel[-1] == "(":
                rel.pop(-1)
            elif s[i] == "}" and rel[-1] == "{":
                rel.pop(-1)
            elif s[i] == "]" and rel[-1] == "[":
                rel.pop(-1)
            else:
                return 0
        if len(rel) == 1:
            return 1
        return 0
