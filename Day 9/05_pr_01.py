with open('/home/cyberboyayush/Documents/Python/Practise/Chapter 9/poems.txt') as f:
    t = f.read()
    if 'twinkle' in t:
        print('twinkle is present')
    else:
        print('twinkle is not present')