import mysql.connector
import ui
class users:
    def __init__(self, host, user, passwd, database, email_id, password):
        self.connection_details = {
            "host" : host,
            "user" : user,
            "passwd" : passwd,
            "database" : database
        }
        self.email_id = email_id
        self.password = password
    def get_quiz_dict(self):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM quiz")
        quiz_tuple = cursor.fetchall()
        quiz_dict = {quiz_id: (quiz_name, topic, difficulty )for quiz_id, quiz_name, topic, difficulty in quiz_tuple}
        cursor.close()
        conn.close()
        return quiz_dict

class user(users):
    def __init__(self, host, user, passwd, database, email_id, password):
        super().__init__(host, user, passwd, database, email_id, password)
    def get_questions_dict(self, quiz_id):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        sqlform = "SELECT question_id, question, option_1, option_2, option_3, option_4, correct_option FROM question WHERE quiz_id = %s"
        parameter = [quiz_id]
        cursor.execute(sqlform, parameter)
        questions = cursor.fetchall()
        questions_dict = {question[0]:question[1:] for question in questions}
        cursor.close()
        conn.close()
        return questions_dict
    def attempt_quiz(self, questions_dict):
        def user_response(question_id, question, option_1, option_2, option_3, option_4):
            print("Question No.:", question_id)
            print("Question:", question)
            print("Options:")
            print("1.", option_1)
            print("2.", option_2)
            print("3.", option_3)
            print("4.", option_4)
            print("Enter the correct option:")
            user_response = ui.checkInt(4)
            print("\n")
            ui.clear()
            return user_response
        response_dict = {question_id : (user_response(question_id, question, option_1, option_2, option_3, option_4), correct_response) for question_id, (question, option_1, option_2, option_3, option_4, correct_response) in questions_dict.items()}
        return response_dict    
    def set_quiz_result(self, quiz_id, response_dict):
        parameter = [[self.email_id, quiz_id, question_id, user_response, correct_response] for question_id, (user_response, correct_response) in response_dict.items()]
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        sqlform = "INSERT INTO result VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(sqlform, parameter)
        conn.commit()
        cursor.close()
        conn.close()
    def check_attempt(self, quiz_id):
        flag = False
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        parameter = [quiz_id, self.email_id]
        sqlform = "SELECT * FROM result WHERE quiz_id = %s AND email_id = %s"
        cursor.execute(sqlform, parameter)
        result = cursor.fetchall()
        if result:
            flag = True
        cursor.close()
        conn.close()
        return flag
    def calc_score_of_attempt(self, response_dict):
        outoff = len(response_dict)
        score = 0
        for i, j in response_dict.values():
            if i == j:
                score += 1
        return (score, outoff )
    def get_attempted_quiz_dict(self):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        cursor.execute("SELECT quiz_id FROM result WHERE email_id = %s", [self.email_id])
        quiz_id_set = set(cursor.fetchall())
        parameters = [[i[0]] for i in quiz_id_set]
        if not parameters:
            return None
        if len(parameters) == 1:
            cursor.execute("SELECT * FROM quiz WHERE quiz_id = %s", parameters[0])
            quiz_tuple = cursor.fetchall()
            quiz_dict = {quiz_id: (quiz_name, topic, difficulty)for quiz_id, quiz_name, topic, difficulty in quiz_tuple}
        else:
            quiz_tuple = []
            for i in parameters:
                cursor.execute("SELECT * FROM quiz WHERE quiz_id = %s", i)
                quiz_tuple.append(cursor.fetchone())
            quiz_dict = {quiz_id: (quiz_name, topic, difficulty)for quiz_id, quiz_name, topic, difficulty in quiz_tuple}
        cursor.close()
        conn.close()
        return quiz_dict
    def print_details_of_attempt(self, quiz_id):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()

        cursor.execute("SELECT question_id, user_response, correct_response FROM result WHERE email_id = %s AND quiz_id = %s", [self.email_id, quiz_id])
        user_response = cursor.fetchall()
        user_response_dict = {question_id: (user_response, correct_response) for question_id, user_response, correct_response in user_response}

        cursor.execute("SELECT question_id, question, option_1, option_2, option_3, option_4 FROM question WHERE quiz_id = %s", [quiz_id])
        questions = cursor.fetchall()
        questions_dict = {question_id: (question, (option_1, option_2, option_3, option_4)) for question_id, question, option_1, option_2, option_3, option_4 in questions}

        cursor.execute("SELECT * FROM user WHERE email_id = %s", [self.email_id])
        user_info = cursor.fetchone()

        cursor.close()
        conn.close()
        
        count = 0
        print("----------------------User Details----------------------")
        print("Name:", user_info[3])
        print("Address:", user_info[4])
        print("Phone No:", user_info[5])
        print("Email ID:", user_info[0])
        print("----------------------Thorough details of this quiz----------------------")
        for question_id in questions_dict.keys():
            print("Question No:", question_id) 
            print("Question:", questions_dict[question_id][0])
            print("Options:")
            for option_no, option in enumerate(questions_dict[question_id][1]):
                print(option_no + 1, ".", option, sep = "")
            user_response = user_response_dict[question_id][0]
            print("Your Response: ", user_response, ".", questions_dict[question_id][1][user_response - 1], sep = "")
            correct_response = user_response_dict[question_id][1]
            print("Correct Response: ", correct_response, ".", questions_dict[question_id][1][correct_response - 1], sep = "")
            score = 0
            if user_response == correct_response:
                score = 1
                count += 1
            print("Score:", score, "\n")
        print("Total Score:", ("/").join([str(count), str(len(questions_dict))]))

class super_user(users):
    def __init__(self, host, user, passwd, database, email_id, password):
        super().__init__(host, user, passwd, database, email_id, password)
    def get_max_quiz_id(self):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(quiz_id) FROM quiz") 
        max_quiz_id = cursor.fetchone()
        cursor.close()
        conn.close()
        return max_quiz_id[0]
    def set_quiz_details(self, quiz_id, quiz_name, topic, difficulty):
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        parameters = [quiz_id, quiz_name, topic, difficulty]
        query = "INSERT INTO quiz VALUES (%s, %s, %s, %s)"
        cursor.execute(query, parameters) 
        conn.commit()
        cursor.close()
        conn.close()
    def set_quiz(self, quiz_id, n):
        parameters = []
        for i in range(1, n + 1):
            while True:
                question = input("Enter Question No {0}(Max 200 characters):\n".format(i))
                if len(question) > 200:
                    ui.clear()
                    print("Max character limit exceeded")
                else:
                    break
            ui.clear()
            options = []
            for j in range(1, 5):
                while True:
                    option = input("Enter option {0}(Max 100 characters):\n".format(j))
                    if len(option) > 100:
                        ui.clear()
                        print("Max character limit exceeded")
                    else:
                        options.append(option)
                        break
            print("Enter correct response(1-4):")
            correct_option = ui.checkInt(4)
            parameters.append([quiz_id, i, question, options[0], options[1], options[2], options[3], correct_option])
        conn = mysql.connector.connect(**self.connection_details)
        cursor = conn.cursor()
        query = "INSERT INTO question VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(query, parameters) 
        conn.commit()
        cursor.close()
        conn.close()

