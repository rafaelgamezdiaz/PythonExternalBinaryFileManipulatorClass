# File Manipulator
# Created by Rafael Gamez Diaz
# 2020

# Imports
import pickle
from datetime import datetime


class WorkingDay:
    """ This class manage the save and edit of a Workday history  """

    def __init__(self, username, action):
        self.username = username
        self.action=action

    def __str__(self):
        self.message_start = self.username + " " + self.action + " workday at ... " + str(datetime.now())
        return "{}".format(self.message_start)


class FileManager:
    history = []

    def __init__(self):

        file = open("workday_history.dat", "ab+")
        file.seek(0)

        try:
            self.history = pickle.load(file)
            print("Loaded ... {} records in the Workday History".format(len(self.history)))
        except:
            print("History is empty")
        finally:
            file.close()
            del file

    def add_record(self, user_record):
        self.history.append(user_record)
        self.save_history_record()

    def add_observation(self, username, obs):
        observations = username + " OBSERVATIONS of day ... " + str(datetime.now()) + ": " + obs
        self.history.append(observations)
        self.save_history_record()

    def show_history(self):
        for record in self.history:
            print(record)

    def save_history_record(self):
        file = open("workday_history.dat", "wb")
        pickle.dump(self.history, file)
        file.close()
        del file


print("***********************")
print("* Workday Desktop App *")
print("***********************\n")
history = FileManager()
workday_option = 0

while workday_option  != '5':

    print("\n\nSelect an Option:")
    print("1 - ) Register start Workday")
    print("2 - ) Register end Workday")
    print("3 - ) Observations of Workday")
    print("4 - ) Show Workday History")
    print("5 - ) Exit")
    print("Option? ", end="")
    workday_option = input()

    if workday_option == '1':
        print("Starting Workday ...")
        print("Enter your name: ", end="")
        name = input()
        new_record = WorkingDay(name, 'start')
        history.add_record(new_record)
        print("Your Starting Workday was registered ...")
    elif workday_option == '2':
        print("Ending Workday ...")
        print("Enter your name: ", end="")
        name = input()
        new_record = WorkingDay(name, 'end')
        history.add_record(new_record)
        print("Your Ending Workday was registered ...")
    elif workday_option == '3':
        print("Record your workday observations ...")
        print("Enter your name: ", end="")
        name = input()
        print("Enter your workday observation: ", end="")
        observation = input()
        history.add_observation(name, observation)
        print("Your workday observations was registered ...")
    elif workday_option == '4':
        print("Workday History ...")
        history.show_history()


print("Thanks for using Workday Desktop App")


