host = input("Enter Host:\n")
user = input("Enter user:\n")
password = input("Enter password:\n")
database = input("Enter database name.(If you have used quiz_database.sql file as SQL source file enter 'quiz_database'):\n")

fo = open("db_info.txt", "w+")
fo.write("host = {0}\nuser = {1}\npassword = {2}\ndatabase = {3}\n".format(host, user, password, database))
fo.close()
print("db_info updated!")
