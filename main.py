from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor

monkey_chicken = Exercise("MonkeyChicken", "Python")
welcome_to_nashville = Exercise("Welcome to Nashville", "JavaScript")
celebrity_tribute = Exercise("Celebrity Tribute", "HTML")
nutshell = Exercise("Nutshell", "ReactJS")

day_cohort_36 = Cohort("Day Cohort 36")
day_cohort_45 = Cohort("Day Cohort 45")
night_cohort_15 = Cohort("Evening Cohort 15")

christian = Student("Christian", "Pippin", "@cpippin98")
lauren = Student("Lauren", "Riddle", "@lriddle19")
corri = Student("Corri", "Golden", "@cgolden17")
matt = Student("Matt", "Blagg", "@mblagg45")
chase = Student("Chase", "Fite", "@cfite76")

day_cohort_36.add_student(christian)
night_cohort_15.add_student(lauren)
day_cohort_45.add_student(corri)
day_cohort_36.add_student(matt)
night_cohort_15.add_student(chase)

joe = Instructor("Joe", "Shepherd", "@jshepherd24", "Python")
jisie = Instructor("Jisie", "David", "@jdavid36", "JavaScript")
jenna = Instructor("Jenna", "Solis", "@jsolis09", "CSharp")

day_cohort_36.add_instructor(joe)
night_cohort_15.add_instructor(jisie)
day_cohort_45.add_instructor(jenna)

joe.assign_exercise(christian, monkey_chicken)