def mirrorChars(input,k):

    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original,reverse))

    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''

    for i in range(0,len(suffix)):
         mirror = mirror + dictChars[suffix[i]]
    print (prefix+mirror)
         
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input,k)
