"""
exercise 1

a- difference between in percent the actual course
the fastest of other courses
the slowest of other courses
the average of all courses

b- percent of unusable material that was reduced on:
the average of all courses
the actual course

c- watch 10 hours of this course and vice versa

"""


dalto_course_time = 1.5
minimal_course_time = 2.5
average_course_time = 4.0
longest_course_time = 7.0

fastest_dif = 100 - dalto_course_time / minimal_course_time * 100
slowest_dif = 100 - dalto_course_time * 1000 // longest_course_time / 10 #a way for controlling decimal numbers
average_dif = 100 - dalto_course_time / average_course_time * 100


print(f"the dalto course have duration {fastest_dif} % more fast in comparison than minimal")
print(f"the dalto course have duration {slowest_dif} % more fast in comparison than longest")
print(f"the dalto course have duration {average_dif} % more fast in comparison than average")
