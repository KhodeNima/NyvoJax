#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database.data import *


def greet():
    """Shows the app greet user prompt"""

    clean()
    loading()
    print(
        f"Welcome to NyvoJax Password Manager version : \33[31m{current_version}\33[34m"
    )
    sleep(4)


def collect_username():
    LOOP1 = True
    LOOP2 = True
    username_confirmation = ""

    clean()
    sleep(4)

    while LOOP1:
        clean()
        if LOOP1 == False:
            break

        print("")
        print(
            "Please note That \33[31musernames\33[34m can only contain \33[31mUpperCase\33[34m , \33[31mLowerCase Letter's\33[34m , \33[31mNumber's \33[34m."
        )
        UserName.inputted_username = input(
            "Please choose a \33[31mUserName\33[34m For Your \33[31m new account\33[34m : "
        )

        if (
            isusername(UserName.inputted_username)
            and UserName.inputted_username not in users_info["Users"].keys()
        ):
            sleep(1)

            clean()

            # Start A while loop In order to repeat the Asking operation.
            while LOOP2:
                clean()

                # Define and if statement to make sure the loop will break Once the Flag variable Is set to False.
                if LOOP2 == False:
                    break

                username_confirmation = input(
                    f"Are You sure you want \33[31m{UserName.inputted_username}\33[34m As your \33[31mAccount UserName\33[34m? (Answer With \33[31myes\33[34m or \33[31mno\33[34m only)  : "
                )
                username_confirmation = username_confirmation.lower()
                username_confirmation = username_confirmation.strip()

                if username_confirmation == "yes":
                    clean()

                    users_info["Users"][UserName.inputted_username] = {}

                    print(
                        f"\33[31m{UserName.inputted_username}\33[34m Has been chosen as your \33[31musername\33[34m."
                    )
                    sleep(3)

                    LOOP1 = False
                    LOOP2 = False
                    break

                elif username_confirmation == "no":
                    clean()

                    print("\33[31mReturning to the login Panel\33[34m. ")
                    sleep(3)
                    break

                else:
                    clean()
                    print(
                        "That Is not a \33[31myes\33[34m or \33[31mno answer \33[34m, Please try again."
                    )
                    sleep(3)

        elif UserName.inputted_username in users_info["Users"].keys():
            clean()

            print(
                "This \33[31m username \33[34m Allready Exist's , Please try a different username"
            )

            input("\33[31mPress any key to continue.\33[34m")

            continue

        else:
            clean()

            print(
                "\33[31 This username does not meet the requirement's to be used.\33[34m \n\
                  Please note that usernames : \n \
                  1. Should Not be less than 3 characters .\n \
                  2. Should Not be more than 13 characters.\n \
                  3. Should Not be number's only.\n \
                  4. Usernames can only contain Uppercase And Lowercase letters , Numbers.  "
            )
            input("\33[31mPress any key to try again\33[34m")


def collect_masterpassword():
    global Inputted_MasterPassword
    Inputted_MasterPassword = None
    confirm_masterpassword = ""
    LOOP1 = True
    LOOP2 = True
    LOOP3 = True

    clean()

    # This Part of the code have been initialized In a while loop In order to avoid Upcoming Errors , DO NOT REMOVE THE WHILE LOOP.
    while LOOP1 == True:
        clean()

        if LOOP1 == False:
            break

        print("This Is the part where you should chose a \33[31mMasterPassword\33[34m.")
        print(
            "This \33[31mMasterPassword\33[34m will be used for accessing your \33[31mAccount\33[34m."
        )
        print(
            f"{color_red}{bold}{format_reversed}Do not{format_reset}{color_blue} share It with anyone."
        )
        print("")
        input("\33[31mPress any key to contoniue.\33[34m")

        LOOP1 = False
        break

    # Define a while loop in Order to loop through the password Choosing Operation.
    while LOOP2 == True:
        clean()

        # Define the loop breaker if statement of the operation. (Flag Variable)
        if LOOP2 == False:
            break

        print(
            "The \33[31mMasterPassword\33[34m at least Must have \33[31m1 Upper Case letter \33[34m, \33[31m1 LowerCase Lettter \33[34m, And at least \33[31mA number.\33[34m"
        )
        Inputted_MasterPassword = input(
            f"Please Chose a \33[31mMasterPassword\33[34m for the {color_red}Account {color_blue} ->  \33[31m{UserName.inputted_username}\33[34m : "
        )
        Inputted_MasterPassword = Inputted_MasterPassword.strip()

        if ismasterpassword(Inputted_MasterPassword):
            # Start a while loop In order to ask the user if their sure about their Inputted MasterPassword.
            while LOOP3:
                clean()

                # Define the loop breaker If statement. (Flag variable)
                if LOOP3 == False:
                    break

                print("Answer with \33[31myes\33[34m or \33[31mno\33[34m only.")
                confirm_masterpassword = input(
                    f"Are You sure you want \33[31m{Inputted_MasterPassword}\33[34m As Your \33[31mMasterPassword \33[34m? : "
                )
                confirm_masterpassword = confirm_masterpassword.lower()
                confirm_masterpassword = confirm_masterpassword.strip()

                # Define an if statement , If the User Is sure about their decision , The MasterPassword Will be On their Username.
                if confirm_masterpassword == "yes".lower():
                    clean()

                    users_info["Users"][UserName.inputted_username] = {}
                    users_info["Users"][UserName.inputted_username][
                        "MasterPassword"
                    ] = Inputted_MasterPassword
                    users_info["Users"][UserName.inputted_username]["PassWords"] = {}

                    clean()

                    print(
                        f"\33[31m{Inputted_MasterPassword}\33[34m Has Been chosen as your \33[31mMasterPassword\33[34m."
                    )
                    sleep(3)
                    clean()
                    LOOP1 = False
                    LOOP2 = False
                    LOOP3 = False
                    break

                # Define an if statement , If the user Change their mind about the Passsword , They will be returned to the password Choosing menu.
                elif confirm_masterpassword == "no".lower():
                    clean()
                    print("\33[31mReturning to the password Choosing Menu...\33[34m")
                    sleep(3)
                    break

        else:
            clean()

            print("\33[34m A Master Password should : \33[31m")
            print(f"{TABS} Contain At Least 1 LowerCase Letter")
            print(f"{TABS} Contain At Least 1 UpperCase Letter")
            print(f"{TABS} Contain At Least 1 Number")
            print(f"{TABS} Contain At Least 5 characters")
            print(f"{TABS} Should Not be longer than 20 characters")
            print("")

            sleep(3)

            input("\33[34mPress any key to continue.")


def collect_birth_date():
    BirthDateFunctionsControl().run()

    if not BirthDateDatabase.accepted_to_add_birthdate:
        users_info["Users"][UserName.inputted_username]["Birth_Date"] = None
        dump_to_json()

    users_info["Users"][UserName.inputted_username][
        "Birth_Date"
    ] = BirthDateDatabase.full_birth_date
    dump_to_json()


def main_menu():
    "-------------------------- Needed Variables ------------------------"
    LOOP1 = True  # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP2 = True  # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP3 = True  # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP4 = True  # Define A bool (True) Variable In order to ube used as FLAG variable in the looping operation.
    LOOP5 = True  # Define A bool (True) Variable In order to be used as FLAG variable in the looping operation.
    LOOP6 = True  # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP7 = True  # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP8 = True  # Define A variable with the bool (True) Value which will be used as the FLAG variable for the looping Operation.
    LOOP9 = True  # Define A bool (True) Variable In order to be used as FLAG varibale in the forgot Password Operation Looping.
    LOOP10 = True  # Define A bool (True) Variable In order to use in the Change User Operation.
    LOOP11 = True  # Define A bool (True) Variable In order to use in the Change User Operation.
    LOOP12 = (
        True  # Define A bool (True) Variable In order to use in the Add user Operation.
    )
    LOOP13 = True  # Flag variable for looping in Delete User.
    masterpassword_input = ""  # Input container for the delete user Operation.
    user_confirmation = ""  # Input Container for the delete user Operation.
    adduser_operation_assurance = ""  # Define A variable with the value of str ("") In order to be used as user Input in the adding user operation , Asking the user if they are sure about Addind A New account or not.
    users_count = len(
        users_info["Users"]
    )  # Define a variable Which keeps the lenght of the Users count as variable.
    changeuser_MasterPassword_Inbox = ""  # Define a variable with the value of str ("") In order to be used as MasterPassword Input in change user Operation.
    ForgotOperation_NewMasterPassword_inbox = ""  # Define A variable with the value of str ("") In order to be used as the NewMasterPassword Input in the forgot Password Operation
    ForgotOperation_BirthDate = ""  # Define A variable with the value of str ("") In order to be used in creating the new BirthDate in the forgot MasterPassword Operation.
    BirthDate_Check = ""  # Define A variable with the value of str ("") In order to be used to check If the user have a existing Birth_Date in their Info or not To be used in the forgot MasterPassword Operation
    Birth_Day_Inbox = ""  # Define A str ("") Variable In order to be used as BirthDay Input identifier In the forgot MasterPassword Operation.
    Birth_Month_Inbox = ""  # Define A str ("") Variable In order to be used as BirthMonth Input Identifier In the forgot MasterPassword Operation.
    Birth_Year_Inbox = ""  # Define A str("") Variable in order to be used as BirthYear Input Identifier In the forgot MasterPassword Operation.
    Current_MasterPassword = users_info["Users"][UserName.inputted_username][
        "MasterPassword"
    ]  # Define a variable with the value of The user Current MasterPassword (Titled) , In order to be used in the MasterPassword Concerned Operation's.
    user_desired_operation = ""  # Define A str ("") Value Variable in Order to be used as the User Input storing Variable , In order to understand what operation they want to use.\
    MasterPassword_Inbox = ""  # Define A str ("") Value variable In order to use as an input , In the changing MasterPassword Operation.
    New_MasterPassword_Inbox = ""  # Define A str ("") Value Variable In order to use as an input , In the changing MasterPassword Operation.
    PassWord_Title = ""  # Define A str ("") Value variable , In order to keep the name of the password.
    Desired_PassWord = ""  # Define A str ("") Value variable in Order to store the password that the user want's to add in the Add_Password.\
    Want_To_Remove = ""  # Define A str("") Value Variable in Order to store the password that Is going to be deleted.
    PassWords = "PassWords"  # Define A str ("PassWords") Value variable in Order to use in A F string print (In order to avoid quotation mark.)
    number = (
        1  # Define A int (1) Value variable In order to use as numbering in the loop.
    )
    "--------------------------------------------------------------------"

    # Start a while Loop With the condition Of the first FLAG variable to be True , In order to LOOP through the menu and It's option's.
    while LOOP1 == True:
        # Note : This Variable Is setted here for ordinary Update , Do Not remove it.
        users_count = len(
            users_info["Users"]
        )  # Define a variable Which keeps the lenght of the Users count as variable.

        clean()

        # Define an If statement , If the First Flag Variable
        if LOOP1 == False:
            break

        print("\33[31m_____________________________________________________\33[34m")
        print(f"Logged Into Account \33[31m ⁛  {UserName.inputted_username} ⁛")
        print("\33[31m_____________________________________________________\33[34m")

        print("")

        print("Here are all the avaliable operation codeNames : ")

        print("")

        for operation_name, operation in operations.items():
            print(f"\33[31m{operation_name} . \33[34m{operation}")

        print(
            "\33[31m---------------------- User Management -----------------------------\33[34m"
        )

        print("")

        for (
            user_operation_number,
            user_management_operation,
        ) in user_management_operations.items():
            print(
                f"\33[31m{user_operation_number} . \33[34m{user_management_operation}"
            )

        print("")

        user_desired_operation = input(
            "Enter the desired \33[31mOperation CodeName\33[34m : "
        )

        if user_desired_operation.isdigit():
            user_desired_operation = int(user_desired_operation)

        else:
            clean()

            print("That Is not a \33[31mknown operation codename\33[34m.")
            print("\33[31mPlease try again\33[34m.")

            sleep(3)

        # VIEW PASSWORD.
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 1
        ]:
            if len(users_info["Users"][UserName.inputted_username]["PassWords"]) == 0:
                clean()

                print(
                    f"You currently Have \33[31mno Password's\33[34m stored . You can store \33[31mpassword's\33[34m in the password \33[31madding\33[34m menu."
                )
                print("Returning to the main menu")

                sleep(5)

                continue

            else:
                clean()

                print("Here Are all the \33[31mPassword's\33[34m You've stored : ")
                print("")

                number = 1

                for PassWord, Title in users_info["Users"][UserName.inputted_username][
                    "PassWords"
                ].items():
                    print(f"{number} . {PassWord} : {Title}")
                    print("")

                    number = number + 1

                print("")
                input("\33[31mPress any key to return to the main menu\33[34m.")

        # ADD PASSWORD.
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 2
        ]:
            LOOP2 = True

            while LOOP2 == True:
                clean()

                if LOOP2 == False:
                    break

                Desired_PassWord = str(
                    input(
                        "Please \33[31menter\33[34m the \33[31mPassword\33[34m you would like to add : "
                    )
                )

                clean()

                PassWord_Title = str(
                    input(
                        "Now Please enter the \33[31mtitle\33[34m you want to specify the \33[31mpassword\33[34m : "
                    )
                )

                clean()

                # This If statement will check ( If the Entered password Is not an empty string and if the entered Password Allready Don't exist in the User passwords )
                if (
                    ispassword(Desired_PassWord)
                    and PassWord_Title
                    not in users_info["Users"][UserName.inputted_username][
                        "PassWords"
                    ].values()
                ):
                    users_info["Users"][UserName.inputted_username]["PassWords"][
                        Desired_PassWord
                    ] = PassWord_Title
                    dump_to_json()

                    print(
                        f" \33[31m{Desired_PassWord}\33[34m Has been added to your password's list as \33[31m{PassWord_Title}\33[34m"
                    )
                    print("Diverting to the main menu.")

                    sleep(5)

                    LOOP2 = False

                elif (
                    PassWord_Title
                    in users_info["Users"][UserName.inputted_username][
                        "PassWords"
                    ].values()
                ):
                    clean()
                    print(
                        "\33[31m That PassWord title allready exists in your password's List , Please assign a new one.\33[34m"
                    )
                    sleep(4)

                elif (
                    Desired_PassWord
                    in users_info["Users"][UserName.inputted_username][
                        "PassWords"
                    ].keys()
                ):
                    clean()
                    print(
                        "\33[31m That Password Allready exist in your password list , Please add a unique one."
                    )
                    sleep(4)
                    clean()

                    continue

        if user_desired_operation in [
            number for number in operations.keys() if number == 3
        ]:
            LOOP3 = True

            while LOOP3:
                if LOOP3 == False:
                    break

                clean()

                if len(users_info["Users"][UserName.inputted_username][PassWords]) == 0:
                    print(
                        "You currently Have no \33[31mPassword\33[34m Stored , You can add password's using the \33[31mAdd\33[34m Password Option In the menu."
                    )
                    print("Diverting Back to the menu...")

                    sleep(4)

                    clean()

                    LOOP3 = False

                else:
                    number = 1

                    for PassWord, PassWord_Title in users_info["Users"][
                        UserName.inputted_username
                    ][PassWords].items():
                        print(
                            f"\33[31m{number}\33[34m . \33[31m{PassWord}\33[34m : {PassWord_Title}"
                        )
                        print("")

                        number = number + 1

                    print(
                        "\33[34m Remember You can type in \33[31mQuit\33[34m Anytime you would like to \33[31mexit\33[34m and return to the main menu.\33[34m"
                    )
                    print("Type in the \33[31mPassWord title \33[34m  Only .")
                    Want_To_Remove = input(
                        "Which One of theese Password's Would you like to \33[31mdelete\33[34m? : "
                    )

                    if Want_To_Remove in [
                        password_title
                        for password_title in users_info["Users"][
                            UserName.inputted_username
                        ]["PassWords"].values()
                        if Want_To_Remove == password_title
                    ]:
                        clean()

                        del users_info["Users"][UserName.inputted_username][
                            "PassWords"
                        ][
                            get_key_by_value(
                                users_info["Users"][UserName.inputted_username][
                                    "PassWords"
                                ],
                                Want_To_Remove,
                            )
                        ]
                        dump_to_json()

                        print(f"\33[31m{PassWord_Title}\33[34m has been deleted.")

                        sleep(4)

                        LOOP3 = False

                    elif Want_To_Remove in QUIT_LETTERCASE:
                        clean()

                        print("\33[31m Diverting back to the menu...\33[34m")

                        sleep(4)

                        clean()

                        LOOP3 = False

                    else:
                        clean()
                        print(
                            "The \33[31m The Chosen Password title Does Not exist. Please try again.\33[34m"
                        )
                        print(
                            "Remember you should mention the password title , Not the password itself."
                        )
                        sleep(4)
                        clean()

                        continue

        # CHANGE MASTERPASSWORD
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 4
        ]:
            LOOP4 = True

            while LOOP4 == True:
                if LOOP4 == False:
                    break

                clean()

                print("Change \33[31mMasterPassWord Menu\33[34m :")
                print("")
                print(
                    "1. Remember You can Insert \33[31mquit\33[34m For returning to the main menu If you changed your mind."
                )

                MasterPassword_Inbox = input(
                    "Please enter your Current \33[31mMasterPassword\33[34m to Resume : "
                )
                MasterPassword_Inbox = MasterPassword_Inbox.strip()

                if MasterPassword_Inbox == Current_MasterPassword:
                    clean()

                    print("Access granted.")

                    sleep(3)

                    LOOP4 = False

                    LOOP5 = True

                    while LOOP5 == True:
                        clean()

                        print(
                            "Remember that If you changed your mind , You can type in \33[31mquit\33[34m for returning to the main menu"
                        )
                        print(
                            "The Inserted \33[31mMasterPassword\33[34m Must Contain At least \33[31m1 UpperCase\33[34m , \33[31mLowerCase Letter\33[34m , And A \33[31mNumbe3\33[34m."
                        )
                        print("")
                        New_MasterPassword_Inbox = input(
                            "Please type In your new MasterPassword : "
                        )
                        New_MasterPassword_Inbox.strip()

                        if ismasterpassword(New_MasterPassword_Inbox):
                            try:
                                users_info["Users"][UserName.inputted_username][
                                    "MasterPassword"
                                ] = New_MasterPassword_Inbox
                                dump_to_json()

                                # Change the current password variable In order to avoid Upcoming Error's everytime the operation Rerun's.
                                Current_MasterPassword = users_info["Users"][
                                    UserName.inputted_username
                                ]["MasterPassword"]

                                clean()

                                print(
                                    f"\33[31m{New_MasterPassword_Inbox}\33[34m Has been set as your \33[31mMasterPassword\33[34m."
                                )

                                sleep(2)

                                print("Diverting to the main menu...")

                                sleep(3)

                                LOOP5 = False

                            except:
                                print(
                                    "The Operation was \33[31munsuccesfull\33[34m , \33[31mPlease try again Later.\33[34m"
                                )

                                LOOP5 = False

                        # Checks if the user Typed in any form of the word "QUIT"
                        elif New_MasterPassword_Inbox in QUIT_LETTERCASE:
                            clean()

                            sleep(1)

                            print("Returning to the main menu...")

                            sleep(3)

                            LOOP5 = False

                        else:
                            clean()

                            print(
                                "The entry Cannot be accepted as A \33[31mMasterPassword\33[34m ,\33[31m Please try again."
                            )

                            sleep(3)

                            continue

                elif MasterPassword_Inbox in QUIT_LETTERCASE:
                    clean()

                    print("The Operation Has been \33[31mCancelled\33[34m.")

                    sleep(2)

                    print("Diverting to the main menu...")

                    sleep(3)

                    break

                else:
                    clean()
                    sleep(2)

                    print("\33[31mAccess Denied.\33[34m")

                    sleep(2)

                    continue

        # FORGOT MasterPassword.
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 5
        ]:
            if users_info["Users"][UserName.inputted_username]["Birth_Date"] is None:
                clean()
                sleep(1)
                print("")

                print(
                    "You Have not added Your \33[31m birthday \33[34m to your \33[31maccount\33[34, , You can't \33[31mrecover\33[34m your \33[31mMasterPassword\33[34m ."
                )

                sleep(5)

                LOOP6 = False

            while LOOP6:
                clean()

                print(
                    "Remember You can type in \33[31mQUIT\33[34m Anytime you have changed your mind."
                )

                print(
                    "Right Now , There Is only \33[31mone solution\33[34m for the \33[31mPassword Recovery\33[34m Operation."
                )

                sleep(2)

                print("")

                Birth_Day_Inbox = input(
                    "Please Type In your \33[31mBirth Day\33[34m (\33[31m1 TO 31\33[34m) : "
                )

                if Birth_Day_Inbox in QUIT_LETTERCASE:
                    break

                if Birth_Day_Inbox.isdigit():
                    Birth_Day_Inbox = int(Birth_Day_Inbox)

                else:
                    clean()

                    print(
                        "The entry Is not a \33[31mnumber\33[34m ,\33[341m Please try again\33[34m."
                    )

                    sleep(2)

                    continue

                if is_birth_day(Birth_Day_Inbox):
                    LOOP7 = True

                    while LOOP7 == True:
                        clean()

                        print(
                            "Remember You can type in \33[31mQUIT\33[34m , for returning to the main menu."
                        )

                        Birth_Month_Inbox = input(
                            "Now Please Type in the \33[31mmonth\33[34m you were born (\33[31m1 to 12\33[34m) :  "
                        )

                        if Birth_Month_Inbox in QUIT_LETTERCASE:
                            LOOP7 = False
                            LOOP6 = False

                        elif Birth_Month_Inbox.isdigit():
                            Birth_Month_Inbox = int(Birth_Month_Inbox)

                            if is_birth_month(Birth_Month_Inbox):
                                LOOP8 = True

                                while LOOP8 == True:
                                    clean()

                                    Birth_Year_Inbox = input(
                                        "At Last , Please type in the \33[31myear\33[34m you were born (\33[31m1923 , 2022\33[34m) : "
                                    )

                                    if Birth_Year_Inbox in QUIT_LETTERCASE:
                                        LOOP6 = False
                                        LOOP7 = False
                                        LOOP8 = False

                                        break

                                    if Birth_Year_Inbox.isdigit():
                                        Birth_Year_Inbox = int(Birth_Year_Inbox)

                                        if isbirthyear(Birth_Year_Inbox):
                                            ForgotOperation_BirthDate = f"{Birth_Day_Inbox}/{Birth_Month_Inbox}/{Birth_Year_Inbox}"

                                            if (
                                                ForgotOperation_BirthDate
                                                == users_info["Users"][
                                                    UserName.inputted_username
                                                ]["Birth_Date"]
                                            ):
                                                LOOP9 = True

                                                while LOOP9 == True:
                                                    clean()

                                                    print(
                                                        "Now , You should enter the \33[31mnew MasterPassword\33[34m you would like."
                                                    )
                                                    print("")
                                                    print(
                                                        "\33[31mMasterPassword\33[34m Must have at \33[31mleast 1 Upper case and lowerCase letter\33[34m , \33[31m1 Number\33[34m , \33[31Shouldn't be less than 5 characters\33[34m."
                                                    )

                                                    ForgotOperation_NewMasterPassword_inbox = input(
                                                        "Please enter the \33[31mnew MasterPassword\33[34m : "
                                                    )
                                                    ForgotOperation_NewMasterPassword_inbox = (
                                                        ForgotOperation_NewMasterPassword_inbox.strip()
                                                    )

                                                    if ismasterpassword(
                                                        ForgotOperation_NewMasterPassword_inbox
                                                    ):
                                                        ForgotOperation_NewMasterPassword_inbox = users_info[
                                                            "Users"
                                                        ][
                                                            UserName.inputted_username
                                                        ][
                                                            "MasterPassword"
                                                        ]
                                                        dump_to_json()

                                                        print(
                                                            f"\33[31m{ForgotOperation_NewMasterPassword_inbox}\33[34m Has been chosen as your \33[31mnew MasterPassword.\33[34m"
                                                        )

                                                        sleep(4)

                                                        LOOP9 = False
                                                        LOOP8 = False
                                                        LOOP7 = False
                                                        LOOP6 = False

                                                    else:
                                                        clean()

                                                        print(
                                                            "Remember that the \33[31mMasterPassword\33[4m should have at least \33[31,1 uppercae letter\33[34m , \33[31m1 LowerCase letter\33[34m , And \33[31m1 number\33[34m."
                                                        )

                                                        print(
                                                            "\33[31mThat Is not a 31mMasterPassword , Please try again.\33[34m"
                                                        )

                                                        sleep(4)

                                            else:
                                                clean()

                                                print(
                                                    "\33[31mAccess denied , Returning to the menu.\33[34m"
                                                )

                                                LOOP6 = False
                                                LOOP7 = False
                                                LOOP8 = False

                                        else:
                                            clean()

                                            print(
                                                "The Inserted Content is not a \33[31mBirthYear\33[34m , Please try again."
                                            )

                                            sleep(4)

                                    else:
                                        clean()

                                        print(
                                            "The inserted content Is not a \33[31mNumber\33[34m , Please try again."
                                        )

                                        sleep(4)

                            else:
                                clean()

                                print(
                                    "The entry Is not a \33[31mbirthmonth\33[34m , Please try again."
                                )

                                sleep(4)

                        else:
                            clean()

                            print(
                                "The entry Is not a \33[31mNumber\33[34m , Please try again."
                            )

                            sleep(4)

                else:
                    clean()

                    print(
                        " The Inserted Number Is not a \33[31mBirthDay\33[34m , \33[31mPlease try again\33[34m."
                    )

                    sleep(4)

        # CHANGE USER.
        if user_desired_operation in [
            Number for Number in user_management_operations.keys() if Number == 7
        ]:
            if users_count == 1:
                clean()

                print(
                    "You Have no other \33[31maccount's\33[34m , You can add Other Account's using \33[31madd user button\33[34m in the menu."
                )

                sleep(4)

                clean()

            else:
                LOOP10 = True

                while LOOP10 == True:
                    clean()

                    print("\33[31mHere are all the avaliable accounts : \33[34m")

                    print("")

                    for user in users_info["Users"]:
                        print(f"⁛  {user} ⁛")

                        print("")

                    sleep(1)

                    print(
                        "Remember you can type in \33[31mquit\33[34m for returning to the main menu , Anytime you desire."
                    )

                    changeuser_username_Inbox = input(
                        f"Which one of the \33[31maccount's\33[34m would you like to Login ? (\33[31mAccount Name\33[34m): {color_blue}"
                    )
                    changeuser_username_Inbox = changeuser_username_Inbox.strip()

                    if (
                        changeuser_username_Inbox
                        in [
                            user
                            for user in users_info["Users"]
                            if changeuser_username_Inbox == user
                        ]
                        and changeuser_username_Inbox != UserName.inputted_username
                    ):
                        clean()

                        LOOP11 = True

                        while LOOP11 == True:
                            clean()

                            changeuser_MasterPassword_Inbox = input(
                                f"\33[34mPlease enter the \33[31m MasterPassword\33[34m For the account \33[31m{changeuser_username_Inbox}\33[0m : "
                            )
                            changeuser_MasterPassword_Inbox = (
                                changeuser_MasterPassword_Inbox.strip()
                            )

                            if (
                                changeuser_MasterPassword_Inbox
                                == users_info["Users"][changeuser_username_Inbox][
                                    "MasterPassword"
                                ]
                            ):
                                clean()

                                print(
                                    f"\33[34m Successfully Logged Into account \33[31m{changeuser_username_Inbox}\33[34m"
                                )

                                UserName.inputted_username = changeuser_username_Inbox

                                sleep(5)

                                LOOP10 = False
                                LOOP11 = False

                            elif changeuser_MasterPassword_Inbox in [
                                quit_type
                                for quit_type in QUIT_LETTERCASE
                                if changeuser_MasterPassword_Inbox == quit_type
                            ]:
                                clean()

                                print("\33[31mQuitting to the main menu.\33[34m")

                                LOOP10 = False
                                LOOP11 = False

                            else:
                                clean()

                                print("\33[31mAccess denied.\33[34m")

                                sleep(3)

                                LOOP11 = False

                    elif changeuser_username_Inbox in [
                        quit_type
                        for quit_type in QUIT_LETTERCASE
                        if changeuser_username_Inbox == quit_type
                    ]:
                        clean()

                        print("\33[31mQuiting to the main menu.\33[34m")

                        sleep(2)

                        LOOP10 = False

                    elif changeuser_username_Inbox == UserName.inputted_username:
                        clean()

                        print(
                            f"\33[31mYou are allready Logged Into account \33[31m{changeuser_username_Inbox} \33[34m"
                        )

                        sleep(4)

                        clean()

                    else:
                        clean()

                        print(
                            "\33[31mThat Account UserName does not exist , try again.\33[34m"
                        )

                        print("")

                        print(
                            "Please note that All \33[31maccount usernames\33[34m are \33[31m cAsE sEnSiTiVe\33[34m"
                        )

                        sleep(5)

        # Add User Operation
        if user_desired_operation in [
            Number for Number in user_management_operations.keys() if Number == 8
        ]:
            LOOP12 = True

            while LOOP12 == True:
                clean()

                adduser_operation_assurance = input(
                    f"Are You \33[31m SURE {color_blue}You  Would like to add \33[31m Another Account\33[34m? (\33[31mYes Or No Only) : {color_blue} "
                )
                adduser_operation_assurance = adduser_operation_assurance.title()

                if adduser_operation_assurance == "Yes":
                    clean()
                    collect_username()
                    collect_masterpassword()
                    collect_birth_date()

                    LOOP12 = False

                    user_desired_operation = None

                elif adduser_operation_assurance == "No":
                    clean()

                    print("\33[31mReturning to the main menu...\33[34m")

                    sleep(4)

                    LOOP12 = False

                else:
                    print(
                        "That Is not A \33[31m Yes \33[34m Or \33[31mNo\33[34m , Please try again"
                    )

                    sleep(4)

                    continue

        # DELETE ACCOUNT.
        if user_desired_operation in [
            Number for Number in user_management_operations.keys() if Number == 9
        ]:
            LOOP13 = True

            while LOOP13 == True:
                clean()

                user_confirmation = input(
                    f"Are You sure You would like to \33[31m Delete the current account\33][34m{color_blue} (\33[31m Yes \33[34m or \33[31m no \33[34m Only) : "
                )
                user_confirmation = user_confirmation.strip()
                user_confirmation = user_confirmation.title()

                if user_confirmation != "Yes" and user_confirmation != "No":
                    clean()

                    print(f"\33[31m Incorrect Entry{color_blue}.")
                    print("\33[34m Please \33[31m Try Again.\33[34m")

                    sleep(3)

                    continue

                elif user_confirmation == "Yes":
                    clean()
                    masterpassword_input = input(
                        "Please enter the \33[31mMasterPassword\33[34m for the \33[31m Current account\33[34m : "
                    )

                    if (
                        equality_check(
                            masterpassword_input,
                            users_info["Users"][UserName.inputted_username][
                                "MasterPassword"
                            ],
                        )
                        == True
                    ):
                        del users_info["Users"][UserName.inputted_username]
                        dump_to_json()

                        clean()
                        print(f"{color_red} Your current account has been deleted.")
                        sleep(3)

                        collect_username()
                        collect_masterpassword()
                        collect_birth_date()

                        clean()

                        LOOP13 = False

                    else:
                        clean()

                        print("\33[31m Access Denied.")
                        sleep(4)

                        LOOP13 = False

                elif user_confirmation == "No":
                    clean()

                    print("\33[31m Returning \33[34m To the \33[31m Main Menu\33[34m")
                    sleep(4)

                    LOOP13 = False

        # Quitting Operation.
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 6
        ]:
            good_bye()


def main():
    greet()
    collect_username()
    collect_masterpassword()
    collect_birth_date()
    main_menu()


if __name__ == "__main__":
    main()

else:
    raise PermissionError("The main package file cannot be imported.")