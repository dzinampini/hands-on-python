def mark_s():

    score = int(input("Enter the mark obtained "))

    if score > 100:
        print("Invalid Score entered, Please enter number between 0 and 100")
    else:
        print("Valid Score")

    if score < 35:
        passneeded = 35 - score
        print("You have failed. You need {} marks to pass".format(passneeded))

    elif score >= 35 and score < 50:
        secondclasspassneeded = 50 - score
        print(
            "You have managed to pass. You need {} marks to get into second class. Work HARDER.".format(
                secondclasspassneeded
            )
        )

    elif score >= 50 and score < 60:
        firstclasspassneeded = 60 - score
        print(
            "You have secured SECOND class. You need {} marks to get into First class. Work HARD.".format(
                firstclasspassneeded
            )
        )

    elif score >= 60 and score < 70:
        Distinctionclasspass = 70 - score
        print(
            "You have secured FIRST class. You need {} marks to get into Distinction class. Push a bit harder.".format(
                Distinctionclasspass
            )
        )

    elif score >= 70:
        if score == 100:
            print("Congratutalations!!! You have secured 100/100. Keep It UP!!!")
        else:
            Tofullmarks = 100 - score
            print(
                "Congratutalations!!! You have secured DISTINCTION class. You need {} marks to get 100/100.".format(
                    Tofullmarks
                )
            )


mark_s()
