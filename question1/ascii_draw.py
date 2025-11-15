
def main():

    while True:
            try:
            
                width = int(input("Enter width (minimum 2): "))
                if width >= 2:
                    break
                else:
                    print ("Error: The width must be atleast 2. Please try again")
            except ValueError:
                print ("Error: Please enter a valid integer")
    
    while True:
            try:

                height = int(input("Enter height (minimum 2): "))
                if height >= 2:
                    break
                else:
                    print ("Error: The height must be at leasee 2. Please try again")
            except ValueError:
                 print ("Error:Please enter a valid integer")
    
    while True:
         char = input("Enter any single character to draw with: ")
         if len(char) == 1:
              break
         else:
              print ("Error: Please enetr exaclty one character")

    def draw_rectangle (width,height,char):

        print (char*width)

        for i in range(height - 2):
            print (char + " " * (width -2) + char)
    
        if height > 1:
            print (char * width)
    
    print ("\nYour Rectangle:\n")
    draw_rectangle(width,height,char)

if __name__ == "__main__":
     main()
