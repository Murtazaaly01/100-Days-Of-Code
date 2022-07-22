text = input("Enter The Text: ")
spam = (
    ("make a lot of money" in text)
    or "buy now" in text
    or "click this" in text
    or "subscribe this" in text
)

if(spam):
    print("This Text Is spam")    
else:
    print("This is not spam")    
