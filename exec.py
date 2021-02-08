import mysql.connector
import users
import ui

def read_db_info():
    fo = open("db_info.txt", "r")
    db_info = fo.readlines()
    db_config = {
        "host" : db_info[0][7: -1],
        "user" : db_info[1][7: -1],
        "passwd" : db_info[2][11: -1],
        "database" : db_info[3][11: -1]
    }
    fo.close()
    return db_config
def check_connection(db_config):
    conn = None
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        conn.close()
        return True
    else:
        return False
def login_validation(email, password, superuser = False):
    flag = False
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if superuser:
        cursor.execute("SELECT email_id, password FROM user WHERE super_user = True")
    else:
        cursor.execute("SELECT email_id, password FROM user WHERE super_user = False")
    user_data = dict(cursor.fetchall())
    if user_data.get(email) == password:
        flag = True
    cursor.close()
    conn.close()
    return flag

#menus
login_menu = ("User Login", "Super User Login", "Quit")
user_home_menu = ("Take Quiz", "Previous Results", "Logout")
super_user_home_menu = ("Set a quiz", "Logout")

while True:
    db_config = read_db_info()
    if check_connection(db_config):
        print("Connection established!!!")
        while True:
            ui.menu(login_menu)
            login_menu_choice = ui.checkInt(len(login_menu))
            if login_menu_choice == 1:
                email_id, password = ui.loginMenu()
                flag = login_validation(email_id, password)
                if flag:
                    user_instance = users.user(**db_config, email_id = email_id, password = password)
                    ui.clear()
                else:
                    print("Incorrect Login Details!!")
                    ui.go_back_menu()                    
                while flag:
                    ui.menu(user_home_menu)
                    user_home_menu_choice = ui.checkInt(len(user_home_menu))
                    if user_home_menu_choice == 1:
                        quiz_id = ui.quiz_menu(user_instance.get_quiz_dict())
                        ui.clear()
                        if user_instance.check_attempt(quiz_id):
                            print("You have already attempted this quiz. For details of your attempt goto 'Previous results' section")
                            ui.go_back_menu()
                        else:
                            questions_dict = user_instance.get_questions_dict(quiz_id)
                            response_dict = user_instance.attempt_quiz(questions_dict)
                            score, outoff = user_instance.calc_score_of_attempt(response_dict)
                            user_instance.set_quiz_result(quiz_id, response_dict)
                            print("Response Collected Succesfully.")
                            print("You scored", score, "Outoff", outoff,"\nFor thorogh review of your attempt goto 'Previous results' section")
                            ui.go_back_menu()
                    elif user_home_menu_choice == 2:
                        quiz_dict = user_instance.get_attempted_quiz_dict()
                        if quiz_dict:
                            print("Quizs that you've attempted so far. Select quiz by it's number id:")
                            quiz_id = ui.quiz_menu(user_instance.get_attempted_quiz_dict())
                            ui.clear()
                            user_instance.print_details_of_attempt(quiz_id)
                        else:
                            print("You haven't attempted any quiz yet. GO to 'Take Quiz' section to attempt quiz")
                        ui.go_back_menu()
                    else:
                        break
            elif login_menu_choice == 2:
                email_id, password = ui.loginMenu()
                flag = login_validation(email_id, password, superuser= True)
                if flag:
                    super_user_instance = users.super_user(**db_config, email_id = email_id, password = password)
                    ui.clear()
                else:
                    print("Incorrect Login Details!!")
                    ui.go_back_menu()
                while flag:
                    ui.menu(super_user_home_menu)
                    super_user_home_menu_choice = ui.checkInt(len(super_user_home_menu))
                    if super_user_home_menu_choice == 1:
                        quiz_id = super_user_instance.get_max_quiz_id() + 1
                        while True:
                            quiz_name = input("Enter Quiz name(Max 50 characters):\n")
                            if len(quiz_name) > 50:
                                ui.clear()
                                print("Max character limit exceeded")
                            else:
                                break
                        ui.clear()
                        while True:
                            topic = input("Enter Quiz topic(Max 50 characters):\n")
                            if len(topic) > 50:
                                ui.clear()
                                print("Max character limit exceeded")
                            else:
                                break
                        ui.clear()
                        print("Enter Quiz difficulty\n1. Easy\n2. Medium\n3. Hard")
                        temp_choice = ui.checkInt(3)
                        temp_dict = {1: "Easy", 2: "Medium", 3: "Hard"}
                        difficulty = temp_dict[temp_choice]
                        ui.clear()
                        super_user_instance.set_quiz_details(quiz_id, quiz_name, topic, difficulty)
                        ui.clear()
                        print("Quiz details entered successfully!\nEnter number of questions in quiz(Max 10):")
                        n = ui.checkInt(10)
                        super_user_instance.set_quiz(quiz_id, n)
                        ui.clear()
                        print("Quiz set succesfully!!!")
                        ui.go_back_menu()
                    else:
                        break
            elif login_menu_choice == 3:
                break
        break    
    else:
        db_config = {}
        print("Can't connect to database!!\nAborting Program!!")
        break



