import schedule
import time
import pyttsx3

class WeeklyPlanner:
    def __init__(self):
        self.todo_list = {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": []
        }
        self.engine = pyttsx3.init()  # Initialize the TTS engine

    def add_task(self, day, task):
        day = day.lower()
        if day in self.todo_list:
            self.todo_list[day].append(task)
            print(f"Task added to {day.capitalize()}'s to-do list: {task}")
        else:
            print("Invalid day. Please enter a valid day of the week.")

    def get_user_input(self):
        for day in self.todo_list:
            task = input(f"Enter a task for {day.capitalize()}: ")
            self.add_task(day, task)

    def display_chart(self):
        print("\nWeekly Task Chart:")
        for day, tasks in self.todo_list.items():
            print(f"{day.capitalize()}:")
            for task in tasks:
                print(f"  - {task}")
            print()  # Add a blank line for readability

    def schedule_tasks(self):
        for day, tasks in self.todo_list.items():
            for task in tasks:
                # Schedule the task to run every day at 10:00 AM (you can customize the time)
                schedule.every().day.at("10:00").do(self.execute_task, task)

    def execute_task(self, task):
        current_time = time.strftime("%H:%M")
        print(f"Executing task: {task} (Current time: {current_time})")

        # Convert task to speech
        self.engine.say(f"It's time to {task}.")
        self.engine.runAndWait()

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    planner = WeeklyPlanner()

    # Get user input for tasks
    planner.get_user_input()

    # Display the weekly task chart
    planner.display_chart()

    # Schedule tasks
    planner.schedule_tasks()

    # Run the scheduler
    planner.run_scheduler()
