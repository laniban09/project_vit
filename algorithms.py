def attendance_percentage(present, total):
    if total <= 0 or present < 0 or present > total:
        raise ValueError("Invalid attendance")
    return present / total * 100


def average_marks(marks):
    if not marks:
        raise ValueError("No marks entered")
    return sum(marks) / len(marks)


def grade_from_percentage(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"
