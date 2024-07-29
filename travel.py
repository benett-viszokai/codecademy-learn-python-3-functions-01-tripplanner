# TripPlanner v1.0

# Welcoming function
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Bennet")

# Estimating the time for the trip
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(10)

# Generating messages
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print('Your trip starts off in ' + origin)
  print('And you are traveling to ' + destination)
  print('You will be traveling by ' + mode_of_transport)
  print('It will take approximately ' + str(estimated_time) + ' hours')

destination_setup("Kiskunlacháza", "Zsámbék", 20, "Majomka")
