#short script to check differences between two datatables in csv format.
#change the file names as needed for the files to be compared. Leave the rest alone.
import csv

#takes in filenames as strings
def file_compare(first_file, second_file):
	with open(first_file, "rb") as orig_file:
		with open(second_file, "rb") as new_file:
			#with open("difffile.csv", "w+") as diff_file:
			#uncomment this if you want to output the result to a new CSV
			reader_1 = csv.reader(orig_file)
			reader_2 = csv.reader(new_file)
			indexed_reader_2 = list(reader_2)
			#writer = csv.writer(diff_file)
			#uncomment this if you want to output the result to a new CSV
			counter = 1
			for i, row_1 in enumerate(reader_1):
				if row_1 != indexed_reader_2[i]:
					#writer.writerow([counter])
					#uncomment this and optionally comment out the print statement below 
					#if you want to output the result to a new CSV
					print(counter)
					counter += 1
				else:
					counter += 1

file_compare(first_file, second_file)