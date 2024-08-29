s='car'
t='cat'
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) !=len(t):
        return(False)
    else:
        if sorted(list(s)) == sorted(list(t)):
            return(True)
        else:
            return(False)
