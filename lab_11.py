#!/usr/bin/env python

number_list = [4986,969,2947,7196,7557,4895,5673,7681,7184,3321,6060,9454,5068,6168,6577,3216,3838,7902,5955,6609,709,9830,7935,1592,2589,8744,2036,7019,9308,8528,6185,6609,6428,6965,4654,1207,8046,9258,6341,2795,2791,5331,3552,9499,3969,8908,6880,638,7733,7887,9661,3457,86,5412,5089,30,1885,2467,9363,6569,1372,2313,2323,7305,1412,739,7434,8196,9501,1039,6040,6447,6525,9308,7523,5110,9150,3092,6874,7,4154,7380,7810,2285,450,960,6130,4931,9163,4277,1973,2096,5554,18,6646,7840,9080,3502,6622,5997]

#using for and if find the smallest, larget and the average number

max_number = None
min_number = None
total_sum = 0
total_numbers = 0


for number in number_list:
    total_numbers += 1
    total_sum += number
    if max_number == None or max_number < number:
        max_number = number
    if min_number == None or min_number > number:
        min_number = number

print "Average number:" + str(float(total_sum)/total_numbers)
print "Max number: " + str(max_number)
print "Min number: " + str(min_number)


