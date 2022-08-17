class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dic={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        word_morse=set()
        for w in words:
            res=""
            for i in w:
                res+=morse_dic[i]
            word_morse.add(res)
            
        return len(word_morse)