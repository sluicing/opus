#!/usr/bin/python -tt

def main():
    words = []
    words.append("a big fireball ")
    words.append("ace your ugly f")
    words.append("this all is om ")
    words.append("n go out and ru")
    words.append("in forth trial ")
    words.append("y and bite pupp")
    words.append("n die again soo")
    words.append("gone with wind ")
    words.append("g bart threw fo")
    words.append("ngs guitar stri")

    #shuffle words here
    
    offsets=[[], [], [], [], []]

    offsets[2] += [ [], [], [],
                    [1,1,1,1],
                    [0,1,1,1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1]]


    for i in range (5):
        for j in range(len(words)):
            # words[j] += words[j][-15:]

            of = offsets[i];
            if len(of) > 0 and j < len(of):
                print "== offset array size:" + str(len(of))
                offset = of[j]
                for k in range(15):
                    # print "."
                    if len(offset) > k and offset[k] > 0:
                        print "-" + str( words[j][-15 + offset[k]]) + "-" + str(words[j][-15])
                        words[j] += words[j][-15 + offset[k]]
                    else :
                        # print "*"
                        words[j] += words[j][-15]
            else:
                words[j] += words[j][-15:]
    

    filename="magic_eye_text.txt"
    print "Output in " + filename
    file=open(filename, "w");
    for line in words:
        file.write(line + "\n")



if __name__ == '__main__':
  main()
