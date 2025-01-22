email = input("Enter your email: ")
k = False
j = False
d = False

# Checking the length
if len(email) >= 6:
    # Checking first charater alphabet hai ki nhi
    if email[0].isalpha():
        # Checking if '@' is present only 1 time
        if "@" in email and email.count("@") == 1:
            # Checking that dot index -4 yafir -3 per hi honi chahiye
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = True
                    elif i.isalpha():
                        # Checking pehla character uppercase hai ke nhi
                        if i.isupper():
                            j = True
                    elif i.isdigit():
                        continue
                    elif i in ["-", ".", "@"]:
                        continue
                    else:
                        d = True

                if k == True or j == True or d == True:
                    print("Invalid email: contains spaces, uppercase letters, or invalid characters.")
                else:
                    print("Valid email.")
            else:
                print("Invalid email: Incorrect position of dot or Incorrect domain .")
        else:
            print("Invalid email: '@' missing or multiple '@' present.")
    else:
        print("Invalid email: First character must be an alphabet.")
else:
    print("Invalid email: Must be at least 6 characters long.")




