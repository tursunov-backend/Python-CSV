import csv

input_file = 'students.csv'

with open(input_file) as f:
    reader = csv.DictReader(f, fieldnames=['name', 'score'])
    next(reader) 

    students = sorted(
        reader,
        key=lambda ball: int(ball['score']),
    )

output_file = 'rating.csv'

with open(output_file, 'w') as f:
    writer = csv.DictWriter(f, fieldnames = ['rank', 'name', 'score'])

    writer.writeheader()

    for i, student in enumerate(students, start=1):
        writer.writerow({
            'rank': i,
            'name': student['name'],
            'score': student['score']
        })

print('rating.csv muvaffaqiyatli yaratildi')
