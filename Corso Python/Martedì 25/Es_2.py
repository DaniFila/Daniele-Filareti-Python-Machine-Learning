def test_palindroma(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


  
def main():
    stringa = input("Inserire la stringa: ")
    stringa_no_space = stringa.replace(" ","")
    print("E' palindroma") if test_palindroma(stringa_no_space) else print("Non è palindroma")    





main()

