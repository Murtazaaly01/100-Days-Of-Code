import os

def isBinod(filename):
    with open(filename , 'r') as f:
        fileContent = f.read()
        #Detect all forms of binod
    return "binod" in fileContent.lower()        

    

if __name__ == "__main__":
    #Listing the content
    dir_contents = os.listdir()
    print(dir_contents)

    nBinod = 0
    #For Each Text file detect binord is them
    for items in dir_contents:
        if items.endswith('txt'):
            print(f'Detecting Binod in {items}')

            if flag := isBinod(items):
                print(f"Binod Found In {items}")
                nBinod += 1
            else:
                print(f"Binod Not FOund in {items}")

print("****Binod Detector Summary****")
print(f'{nBinod} is founded in {items}')