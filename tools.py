from datetime import datetime

def calculate_bmi(weight, height):
    """
    Calculate BMI
    weight -> kilograms
    height -> meters
    """

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return f"BMI: {round(bmi,2)} ({category})"


def calculate_age(birth_year):
    """
    Calculate age from birth year
    """

    current_year = datetime.now().year
    age = current_year - birth_year

    return f"Age: {age} years"


def calculate_grade(mark):
    """
    Calculate grade from marks
    """

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "Fail"

    return f"Grade: {grade}"