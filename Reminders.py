

def ask():
    reminder = input("Set a reminder for Monday(m), Tuesday(h), Wednesday(w), Thursday(t), Friday(f), Saturday(s), Sunday(a).")


    while (reminder != 'q'):



        if reminder == 'm':
            m = input("Enter what you have to do on Monday.")


        elif reminder == 't':
            t = input("Enter what you have to do on Tuesday.")


        elif reminder == 'w':
            w = input("Enter what you have to do on Wednesday.")


        elif reminder == 'h':
            h = input("Enter what you have to do on Thursday.")


        elif reminder == 'f':
            f = input("Enter what you have to do on Friday.")


        elif reminder == 's':
            s = input("Enter what you have to do on Saturday.")


        elif reminder == 'a':
            a = input("Enter what you have to do on Sunday.")


        else:
            print("Sorry please try again or please set a reminder before viewing it.")

            reminder = input("Set a reminder for Monday(m), Tuesday(h), Wednesday(w), Thursday(t), Friday(f), Saturday(s), Sunday(a).")




