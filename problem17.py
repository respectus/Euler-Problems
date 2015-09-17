

def answer():
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen", 
             "seventeen","eighteen","nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    num_words = []

    for x in range(1001):
        if x < 9:
            num_words.append(ones[x])
        if x == 10:
            num_words.append(tens[0])
        if x > 10 and x < 20 :
            num_words.append(teens[x%10 - 1])
        if x >= 20 and x < 100:
            if x%10 == 0:
                num_words.append(tens[x//10 - 1])
            else:
                num_words.append(tens[x//10 - 1] + ones[x%10 - 1])
        if x == 100:
            num_words.append("onehundred")
        if x > 100 and x < 1000:
            num = x - (x//100 * 100)
            if num < 10 and num%10 > 0:
                num_words.append(ones[x//100 - 1] + "hundredand" + ones[x%10 - 1])
            if num == 10:
                num_words.append(ones[x//100 - 1] + "hundredand" + tens[0])
            if num > 10 and num < 20 :
                num_words.append(ones[x//100 - 1] + "hundredand" + teens[x%10 - 1])
            if num >= 20 and num < 100:
                if num%10 == 0:
                    num_words.append(ones[x//100 - 1] + "hundredand" + tens[(x-(x//100 *100))//10 - 1])
                else:
                    num_words.append(ones[x//100 - 1] + "hundredand"+ tens[(x-(x//100 *100))//10 - 1] + ones[x%10 - 1])
            if x%10 == 0 and (x//10)%10 == 0 and x != 1000:
                num_words.append( ones[x//100 - 1]+"hundred") 

        if x == 1000:
            num_words.append("onethousand")

    #print("\n".join(num_words))
    print(sum(map(len, num_words)))

