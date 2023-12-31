#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# The main NyoJax PasswordManager file
---
- Raises:
    - PermissionError: If the file is imported (` This file cannot be imported and must run directly as script `).
---
# KhodeNima
# 2023/10/27
---
"""

from database.data import __version__
from database.data import *


def greet():
    """Shows the app greeting user prompt"""

    clean()
    clean()
    print(
        f"Welcome to NyvoJax password manager version : {COLOR_RED}{__version__}{COLOR_BLUE}."
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
            "Please note that \33[31musernames\33[34m can only contain \33[31mUpperCase\33[34m , \33[31mLowerCase Letter's\33[34m , \33[31mNumber's \33[34m."
        )

        Username.inputted_username = input(
            "Please choose a \33[31musername\33[34m For Your \33[31m new account\33[34m : "
        )

        if (
            isusername(Username.inputted_username)
            and Username.inputted_username not in users_info["users"].keys()
        ):
            sleep(1)

            clean()

            while LOOP2:
                clean()

                if not LOOP2:
                    break

                username_confirmation = input(
                    f"Are you sure want \33[31m{Username.inputted_username}\33[34m As your \33[31mAccount UserName\33[34m? (Answer With \33[31myes\33[34m or \33[31mno\33[34m only)  : "
                )
                username_confirmation = username_confirmation.lower()
                username_confirmation = username_confirmation.strip()

                if username_confirmation == "yes":
                    clean()

                    users_info["users"][Username.inputted_username] = {}

                    print(
                        f"\33[31m{Username.inputted_username}\33[34m have been chosen as your \33[31musername\33[34m."
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
                        "That is not a \33[31myes\33[34m or \33[31mno answer \33[34m, Please try again."
                    )
                    sleep(3)

        elif Username.inputted_username in users_info["users"].keys():
            clean()

            print(
                f"This {COLOR_RED} username {COLOR_BLUE} allready exist. Please try a different {COLOR_RED} username {COLOR_BLUE}"
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
            input("\33[31mPress any key to try again\33[34m ")


def collect_masterpassword():
    global inputted_masterpassword
    inputted_masterpassword = None
    confirm_masterpassword = ""
    LOOP1 = True
    LOOP2 = True
    LOOP3 = True

    clean()

    while LOOP1 == True:
        clean()

        if LOOP1 == False:
            break

        print("This is the part where you should chose a \33[31mMasterPassword\33[34m.")
        print(
            "This \33[31mMasterPassword\33[34m will be used for accessing your \33[31mAccount\33[34m."
        )
        print(
            f"{COLOR_RED}{bold}{format_reversed}Do not{format_reset}{COLOR_BLUE} share It with anyone."
        )
        print("")
        input("\33[31mPress any key to contoniue.\33[34m")

        LOOP1 = False
        break

    while LOOP2 == True:
        clean()

        if LOOP2 == False:
            break

        print(
            "The \33[31mMasterPassword\33[34m at least Must have \33[31m1 Upper Case letter \33[34m, \33[31m1 LowerCase Lettter \33[34m, And at least \33[31mA number.\33[34m"
        )
        inputted_masterpassword = input(
            f"Please Chose a \33[31mMasterPassword\33[34m for the {COLOR_RED}Account {COLOR_BLUE} ->  \33[31m{Username.inputted_username}\33[34m : "
        )
        inputted_masterpassword = inputted_masterpassword.strip()

        if ismasterpassword(inputted_masterpassword):
            while LOOP3:
                clean()

                if LOOP3 == False:
                    break

                print("Answer with \33[31myes\33[34m or \33[31mno\33[34m only.")
                confirm_masterpassword = input(
                    f"Are you sure you want \33[31m{inputted_masterpassword}\33[34m As Your \33[31mMasterPassword \33[34m? : "
                )
                confirm_masterpassword = confirm_masterpassword.lower()
                confirm_masterpassword = confirm_masterpassword.strip()

                if confirm_masterpassword == "yes".lower():
                    clean()

                    users_info["users"][Username.inputted_username] = {}
                    users_info["users"][Username.inputted_username][
                        "MasterPassword"
                    ] = inputted_masterpassword
                    users_info["users"][Username.inputted_username]["PassWords"] = {}

                    clean()

                    print(
                        f"{COLOR_RED}{inputted_masterpassword} {COLOR_BLUE} Has Been chosen as your{COLOR_RED} MasterPassword{COLOR_BLUE}."
                    )
                    sleep(3)
                    clean()
                    LOOP1 = False
                    LOOP2 = False
                    LOOP3 = False
                    break

                elif confirm_masterpassword == "no".lower():
                    clean()
                    print("\33[31mReturning to the password Choosing Menu...\33[34m")
                    sleep(3)
                    break

        else:
            clean()

            print("\33[34m A Master Password should : \33[31m")
            print(f"{TAB} Contain At Least 1 LowerCase Letter")
            print(f"{TAB} Contain At Least 1 UpperCase Letter")
            print(f"{TAB} Contain At Least 1 Number")
            print(f"{TAB} Contain At Least 5 characters")
            print(f"{TAB} Should Not be longer than 20 characters")
            print("")

            sleep(3)

            input("\33[34mPress any key to continue.")


def collect_birth_date():
    BirthDateFunctionsControl().run()

    if not BirthDateDatabase.accepted_to_add_birthdate:
        users_info["users"][Username.inputted_username]["Birth_Date"] = None
        dump_to_database()

    users_info["users"][Username.inputted_username][
        "Birth_Date"
    ] = BirthDateDatabase.full_birth_date

    BirthDateFunctions.reset_all_birth_operation_variables()
    dump_to_database()


def sign_in():
    collect_username()
    collect_masterpassword()
    collect_birth_date()


def main_menu():
    """# The programs main menu
    ---
    - WARNING : Must be logged-in to use.
    """
    dump_to_database()
    load_from_database()

    LOOP1 = True
    LOOP2 = True
    LOOP3 = True
    LOOP4 = True
    LOOP5 = True
    LOOP6 = True
    LOOP7 = True
    LOOP8 = True
    LOOP9 = True
    LOOP10 = True
    LOOP11 = True
    LOOP12 = True
    LOOP13 = True
    masterpassword_input = ""
    user_confirmation = ""
    adduser_operation_assurance = ""
    users_count = len(users_info["users"])
    changeuser_MasterPassword_Inbox = ""
    forgot_operation_newpass_inbox = ""
    forgotoperation_birthdate_input = ""
    BirthDate_Check = ""
    birth_year_inbox = ""
    current_user = Username.inputted_username
    Current_MasterPassword = users_info["users"][Username.inputted_username][
        "MasterPassword"
    ]
    user_desired_operation = ""
    MasterPassword_Inbox = ""
    New_MasterPassword_Inbox = ""
    PassWord_Title = ""
    Desired_PassWord = ""
    Want_To_Remove = ""
    PassWords = users_info["users"][Username.inputted_username]["PassWords"].keys()
    number = ()

    while LOOP1 == True:
        users_count = len(users_info["users"])

        clean()

        if LOOP1 == False:
            break

        print(f"{COLOR_RED} {format_character} {COLOR_BLUE}")
        print(f"   Logged into account \33[31m ⁛  {Username.inputted_username} ⁛")
        print(f"{COLOR_RED} {format_character} {COLOR_BLUE}")

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
            "Enter the desired \33[31moperation number\33[34m : "
        )

        if user_desired_operation.isdigit():
            user_desired_operation = int(user_desired_operation)

        else:
            clean()

            print("That is not a \33[31mknown operation number\33[34m.")
            print("\33[31mPlease try again\33[34m.")

            sleep(3)

        # VIEW PASSWORD.
        if user_desired_operation in [
            Number for Number in operations.keys() if Number == 1
        ]:
            if len(users_info["users"][Username.inputted_username]["PassWords"]) == 0:
                clean()

                print(
                    f"You currently Have \33[31mno passwords\33[34m stored ; you can store\33[31m passwords\33[34m in the password\33[31 madding\33[34m menu."
                )
                print("Returning to the main menu")

                sleep(5)

                continue

            else:
                clean()

                print("Here Are all the \33[31mPassword's\33[34m You've stored : ")
                print("")

                number = 1

                for PassWord, Title in users_info["users"][Username.inputted_username][
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

                if (
                    ispassword(Desired_PassWord)
                    and PassWord_Title
                    not in users_info["users"][Username.inputted_username][
                        "PassWords"
                    ].values()
                ):
                    users_info["users"][Username.inputted_username]["PassWords"][
                        Desired_PassWord
                    ] = PassWord_Title
                    dump_to_database()

                    print(
                        f" \33[31m{Desired_PassWord}\33[34m Has been added to your password's list as \33[31m{PassWord_Title}\33[34m"
                    )
                    print("Diverting to the main menu.")

                    sleep(5)

                    LOOP2 = False

                elif (
                    PassWord_Title
                    in users_info["users"][Username.inputted_username][
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
                    in users_info["Users"][Username.inputted_username][
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

                if len(users_info["users"][Username.inputted_username][PassWords]) == 0:
                    print(
                        "You currently Have no \33[31mPassword\33[34m Stored , You can add password's using the \33[31mAdd\33[34m Password Option In the menu."
                    )
                    print("Diverting Back to the menu...")

                    sleep(4)

                    clean()

                    LOOP3 = False

                else:
                    number = 1

                    for PassWord, PassWord_Title in users_info["users"][
                        Username.inputted_username
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
                        for password_title in users_info["users"][
                            Username.inputted_username
                        ]["PassWords"].values()
                        if Want_To_Remove == password_title
                    ]:
                        clean()

                        del users_info["users"][Username.inputted_username][
                            "PassWords"
                        ][
                            get_key_by_value(
                                users_info["users"][Username.inputted_username][
                                    "PassWords"
                                ],
                                Want_To_Remove,
                            )
                        ]
                        dump_to_database()

                        print(f"\33[31m{PassWord_Title}\33[34m has been deleted.")

                        sleep(4)

                        LOOP3 = False

                    elif Want_To_Remove in VALID_QUIT_VALUES:
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

                print("Change \33[31m MasterPassWord Menu\33[34m :")
                print("")
                print(
                    "1. Remember you can type in \33[31mquit\33[34m For returning to the main menu If you changed your mind."
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
                            "Remember that if you changed your mind , You can type in \33[31mquit\33[34m for returning to the main menu"
                        )
                        print(
                            "The inserted \33[31mMasterPassword\33[34m must contain at least\33[31m 1 UpperCase\33[34m , \33[31mLowerCase Letter\33[34m , And A \33[31mNumbe3\33[34m."
                        )
                        print("")
                        New_MasterPassword_Inbox = input(
                            "Please type In your new MasterPassword : "
                        )
                        New_MasterPassword_Inbox.strip()

                        if ismasterpassword(New_MasterPassword_Inbox):
                            try:
                                users_info["users"][Username.inputted_username][
                                    "MasterPassword"
                                ] = New_MasterPassword_Inbox
                                dump_to_database()

                                # Change the current password variable In order to avoid Upcoming Error's everytime the operation Rerun's.
                                Current_MasterPassword = users_info["users"][
                                    Username.inputted_username
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

                        elif New_MasterPassword_Inbox in VALID_QUIT_VALUES:
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

                elif MasterPassword_Inbox in VALID_QUIT_VALUES:
                    clean()

                    print("The operation have been \33[31mcancelled\33[34m.")

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

        # Forgot MasterPassword.
        if user_desired_operation in [
            number for number in operations.keys() if number == 5
        ]:
            LOOP6 = True
            if users_info["users"][Username.inputted_username]["Birth_Date"] is None:
                clean()
                sleep(1)
                print("")

                print(
                    "You Have not added Your \33[31m birthday \33[34m to your \33[31m account\33[34, , You can't \33[31m recover\33[34m your \33[31mMasterPassword\33[34m ."
                )

                sleep(5)

                LOOP6 = False

            while LOOP6:
                clean()

                print(
                    f"Remember You can type in {COLOR_RED}QUIT{COLOR_BLUE} Anytime you have changed your mind."
                )

                print(
                    "Right Now , There is only \33[31mone solution\33[34m for the \33[31mPassword Recovery\33[34m Operation."
                )

                sleep(2)

                print("")

                birth_day_inbox = input(
                    "Please Type In your \33[31mBirth Day\33[34m (\33[31m1 TO 31\33[34m) : "
                )

                if birth_day_inbox in VALID_QUIT_VALUES:
                    break

                if birth_day_inbox.isdigit():
                    birth_day_inbox = int(birth_day_inbox)

                else:
                    clean()

                    print(
                        f"The entry iss not a {number}number{COLOR_BLUE} ,{COLOR_RED} Please try again{COLOR_BLUE}."
                    )

                    sleep(2)

                    continue

                if is_birth_day(birth_day_inbox):
                    LOOP7 = True

                    while LOOP7 == True:
                        clean()

                        print(
                            "Remember You can type in \33[31mQUIT\33[34m , for returning to the main menu."
                        )

                        birth_month_inbox = input(
                            "Now Please Type in the \33[31mmonth\33[34m you were born (\33[31m1 to 12\33[34m) :  "
                        )

                        if birth_month_inbox in VALID_QUIT_VALUES:
                            LOOP7 = False
                            LOOP6 = False

                        elif birth_month_inbox.isdigit():
                            birth_month_inbox = int(birth_month_inbox)

                            if is_birth_month(birth_month_inbox):
                                LOOP8 = True

                                while LOOP8 == True:
                                    clean()

                                    birth_year_inbox = input(
                                        f"At Last , Please type in the {COLOR_RED}year {COLOR_BLUE} you were born ({COLOR_RED}1923{COLOR_BLUE} to {COLOR_RED}2022{COLOR_BLUE}) : "
                                    )

                                    if birth_year_inbox in VALID_QUIT_VALUES:
                                        LOOP6 = False
                                        LOOP7 = False
                                        LOOP8 = False

                                        break

                                    if birth_year_inbox.isdigit():
                                        birth_year_inbox = int(birth_year_inbox)

                                        if isbirthyear(birth_year_inbox):
                                            forgotoperation_birthdate_input = f"{birth_day_inbox}/{birth_month_inbox}/{birth_year_inbox}"

                                            if (
                                                forgotoperation_birthdate_input
                                                == users_info["users"][
                                                    Username.inputted_username
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
                                                        f"{COLOR_RED}MasterPassword{COLOR_BLUE} Must have {COLOR_RED}at least 1 Upper case {COLOR_BLUE} and {COLOR_RED} lowerCase letter {COLOR_BLUE}, {COLOR_RED} Number {COLOR_BLUE} and {COLOR_RED} Shouldn't be less than 5 characters{COLOR_BLUE}."
                                                    )

                                                    forgot_operation_newpass_inbox = input(
                                                        f"Please enter the {COLOR_RED}new MasterPassword{COLOR_BLUE} : "
                                                    )
                                                    forgot_operation_newpass_inbox = (
                                                        forgot_operation_newpass_inbox.strip()
                                                    )

                                                    if ismasterpassword(
                                                        forgot_operation_newpass_inbox
                                                    ):
                                                        users_info["users"][
                                                            current_user
                                                        ][
                                                            "MasterPassword"
                                                        ] = forgot_operation_newpass_inbox
                                                        dump_to_database()

                                                        clean()
                                                        print(
                                                            f"{COLOR_RED}{forgot_operation_newpass_inbox} {COLOR_BLUE }Has been chosen as your {COLOR_RED}new MasterPassword. {COLOR_BLUE}"
                                                        )

                                                        sleep(4)

                                                        LOOP9 = False
                                                        LOOP8 = False
                                                        LOOP7 = False
                                                        LOOP6 = False

                                                    else:
                                                        clean()

                                                        print(
                                                            f"Remember that the {COLOR_RED}MasterPassword {COLOR_BLUE} should have at least {COLOR_RED} uppercae letter {COLOR_BLUE}, {COLOR_RED}1 LowerCase letter{COLOR_BLUE} , And {COLOR_RED}1 number {COLOR_BLUE}."
                                                        )

                                                        print(
                                                            f"{COLOR_BLUE}That is not a {COLOR_RED}MasterPassword {COLOR_BLUE}, Please try again. {COLOR_BLUE}"
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
                                                "The inserted content is not a \33[31mBirthYear\33[34m , Please try again."
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
                                    f"The entry iss not a {COLOR_RED}birthmonth {COLOR_BLUE}, Please try again."
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
                        "The inserted number Is not a \33[31mBirthDay\33[34m , \33[31mPlease try again\33[34m."
                    )

                    sleep(4)

        # CHANGE USER.
        if user_desired_operation in [
            Number for Number in user_management_operations.keys() if Number == 7
        ]:
            if users_count == 1:
                clean()

                print(
                    f"You Have no other {COLOR_RED}accounts{COLOR_BLUE}; You can add Other ccounts using {COLOR_RED}the add user option {COLOR_BLUE} in the menu."
                )

                sleep(4)

                clean()

            else:
                LOOP10 = True
                LOOP11 = True

                while LOOP10 == True:
                    clean()

                    print(
                        "\33[31mHere are all the avaliable accounts on this device : \33[34m"
                    )

                    print("")

                    for user in users_info["users"]:
                        print(f"⁛  {user} ⁛")

                        print("")

                    sleep(1)

                    print(
                        "Remember you can type in \33[31mquit\33[34m for returning to the main menu , Anytime you desire."
                    )

                    changeuser_username_Inbox = input(
                        f"Which one of the \33[31maccounts\33[34m would you like to Login ? ({COLOR_RED}Account Name {COLOR_BLUE} ): {COLOR_BLUE}"
                    )
                    changeuser_username_Inbox = changeuser_username_Inbox.strip()

                    if (
                        changeuser_username_Inbox
                        in [
                            user
                            for user in users_info["users"]
                            if changeuser_username_Inbox == user
                        ]
                        and changeuser_username_Inbox != Username.inputted_username
                    ):
                        clean()

                        LOOP11 = True

                        while LOOP11 == True:
                            clean()

                            changeuser_MasterPassword_Inbox = input(
                                f"\33[34mPlease enter the \33[31m MasterPassword\33[34m For the account \33[31m{changeuser_username_Inbox}{COLOR_BLUE}: "
                            )
                            changeuser_MasterPassword_Inbox = (
                                changeuser_MasterPassword_Inbox.strip()
                            )

                            if (
                                changeuser_MasterPassword_Inbox
                                == users_info["users"][changeuser_username_Inbox][
                                    "MasterPassword"
                                ]
                            ):
                                clean()

                                print(
                                    f"\33[34m Successfully Logged Into account \33[31m{changeuser_username_Inbox}\33[34m"
                                )

                                Username.inputted_username = changeuser_username_Inbox

                                sleep(5)

                                LOOP10 = False
                                LOOP11 = False

                            elif changeuser_MasterPassword_Inbox in [
                                quit_type
                                for quit_type in VALID_QUIT_VALUES
                                if changeuser_MasterPassword_Inbox == quit_type
                            ]:
                                clean()

                                print(
                                    f"{COLOR_RED} Returning to the main menu. {format_reset}"
                                )

                                LOOP10 = False
                                LOOP11 = False

                            else:
                                clean()

                                print("\33[31mAccess denied.\33[34m")

                                sleep(3)
                                LOOP11 = False

                    elif changeuser_username_Inbox in [
                        quit_type
                        for quit_type in VALID_QUIT_VALUES
                        if changeuser_username_Inbox == quit_type
                    ]:
                        clean()

                        print("\33[31mQuiting to the main menu.\33[34m")

                        sleep(2)

                        LOOP10 = False

                    elif changeuser_username_Inbox == Username.inputted_username:
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
                    f"Are You \33[31m SURE {COLOR_BLUE}You  Would like to add \33[31m Another Account\33[34m? ( \33[31mYes or no only ) : {COLOR_BLUE} "
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
                        "That is not A \33[31m Yes \33[34m Or \33[31mNo\33[34m , Please try again"
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
                    f"Are you sure You would like to \33[31m Delete the current account\33][34m{COLOR_BLUE} (\33[31m Yes \33[34m or \33[31m no \33[34m Only) : "
                )
                user_confirmation = user_confirmation.strip()
                user_confirmation = user_confirmation.title()

                if user_confirmation != "Yes" and user_confirmation != "No":
                    clean()

                    print(f"\33[31m Incorrect Entry{COLOR_BLUE}.")
                    print("\33[34m Please \33[31m Try Again.\33[34m")

                    sleep(3)

                    continue

                elif user_confirmation == "Yes":
                    clean()
                    masterpassword_input = input(
                        f"Please enter the \33[31mMasterPassword\33[34m for the \33[31m Current account ( {Username.inputted_username} )\33[34m : "
                    )

                    if (
                        equality_check(
                            masterpassword_input,
                            users_info["users"][Username.inputted_username][
                                "MasterPassword"
                            ],
                        )
                        == True
                    ):
                        del users_info["users"][Username.inputted_username]
                        dump_to_database()

                        clean()
                        print(f"{COLOR_RED} Your current account has been deleted.")
                        sleep(3)

                        collect_username()
                        collect_masterpassword()
                        collect_birth_date()

                        clean()

                        LOOP13 = False

                    else:
                        clean()

                        print(f"{COLOR_RED} Access Denied{COLOR_BLUE}.")
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
            farewell_user()
            close_safely()


def main():
    loading_screen()
    greet()
    sign_in()
    main_menu()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        sleep(1.5)
        clean()
        print(f"{COLOR_RED} the application have been interrupted{COLOR_BLUE}.")
        sleep(2)
        farewell_user()
        close_safely()

else:
    raise PermissionError("The main package file cannot be imported.")
