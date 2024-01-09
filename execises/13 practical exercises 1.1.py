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
#duration average
dalto_course_time = 1.5
minimal_course_time = 2.5
average_course_time = 4.0
longest_course_time = 7.0

#this way gets a proportion, for example gets 1/4 and so on

fastest_dif = 100 - dalto_course_time / minimal_course_time * 100
slowest_dif = 100 - dalto_course_time * 1000 // longest_course_time / 10 #a way for controlling decimal numbers
average_dif = 100 - dalto_course_time / average_course_time * 100

print("-------------------------------")

#a-
print(f"the dalto course have duration {fastest_dif} % more fast in comparison than minimal")
print(f"the dalto course have duration {slowest_dif} % more fast in comparison than longest")
print(f"the dalto course have duration {average_dif} % more fast in comparison than average")

#duration raw files
raw_average = 5
raw_dalto = 3.5 

raw_difference = 100 - raw_dalto / raw_average * 100
raw_difference_compared_other_courses = 100 - dalto_course_time / raw_average * 100

print("-------------------------------")

#b-
print(f"the dalto course reduces, in {raw_difference}% percentage")
print(f"the dalto course reduces, in {raw_difference_compared_other_courses}% percentage, compared with other courses")

print("-------------------------------")

#c-
print(f"course equivalency of this course 10 hours {average_course_time *100 // dalto_course_time / 10} hours equivalency")
print(f"course equivalency of other courses 10 hours { dalto_course_time *100 // average_course_time / 10} hours equivalency")
