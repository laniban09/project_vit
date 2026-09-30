# Design Notes

## How I planned the program

I first listed the things the program should do: store students, record attendance, enter marks and show a simple result. I then wrote the menu and added each option one at a time.

Because this is a small project, I kept most of the code in `main.py`. At first I had separate files for almost every small part, but that made the project harder to follow. Keeping the main functions together felt easier to understand for this project.

## Data used

The program stores three main sections in `data.json`:

- students
- attendance
- marks

The student ID is used to connect these sections.

## Main calculations

Attendance percentage is:

`(classes attended / total classes) × 100`

For marks, the program adds the subject marks and divides by the number of subjects. The average is then compared with the grade ranges used in the program.

## Input checking

I added simple checks for things such as empty student details, invalid marks and attendance values. This prevents common input mistakes from stopping the program.

## Basic flow

Start → show menu → choose an option → take input → process the data → save or display the result → show the menu again.

## Why I used JSON

I used JSON because it was enough for a small project and did not require setting up a separate database. If the project becomes larger, a database would make more sense.
