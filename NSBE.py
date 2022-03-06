
1 of 9,316
(no subject)
Inbox

Ashvat Ranadive
Attachments
11:23 AM (0 minutes ago)
to me


Attachments area
# orange - pronouns
# white - connectives
# blue - racial terms
# black - derogatory terms
orange = ['he', 'her', 'she', 'him', 'you', 'them', 'they', 'it', 'my']
white = ['are', 'moreover', 'because', 'thus', 'consequently', 'then', 'instead', 'however', 'is']
blue = ['a', 'b', 'c', 'd', 'e']
black = ['apple', 'banana', 'mango', 'orange']

sent = [input("enter a sentence")]
sent_words = [i for item in sent for i in item.split()]
o, w, b, bl = 0, 0, 0, 0
for wrd in sent_words:
    if wrd in orange:
        o += 1
        print('orange', end=' ')
    elif wrd in white:
        w += 1
        print('white', end=' ')
    elif wrd in blue:
        b += 1
        print('blue', end=' ')
    elif wrd in black:
        bl += 1
        print('black', end=' ')
    else:
        print("invalid", end=' ')
print('')
print('orange :' + str(o), end=' ')
print('white :' + str(w), end=' ')
print('blue :' + str(b), end=' ')
print('black :' + str(bl), end=' ')
