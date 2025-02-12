def enrollment_stats(uni) :
    enrollments = [x[1] for x in uni]
    tuitions = [x[2] for x in uni]
    return enrollments, tuitions

def mean(values):
    return round(sum(values) / len(values) , 2)

def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        mid1, mid2 = values[n // 2 - 1], values[n // 2]
        return (mid1 + mid2) / 2


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments, tuitions = enrollment_stats(universities)
total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_enrollment = mean(enrollments)
median_enrollment = median(enrollments)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("Total Students:", total_students)
print("Total Tuition:", total_tuition)
print("Mean Enrollment:", mean_enrollment)
print("Median Enrollment:", median_enrollment)
print("Mean Tuition:", mean_tuition)
print("Median Tuition:", median_tuition)
