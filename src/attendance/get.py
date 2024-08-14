import time


def get_date():
    date = input("Date (DDMMYY): ")
    try:
        time.strptime(date, "%d%m%y")
    except ValueError as e:
        print("Date must be in DDMMYY format", e)
        return get_date()
    else:
        return date


def get_time(time_type):
    return_time = input(f"Lesson {time_type} Time (HHMM): ")
    try:
        time.strptime(return_time, "%H%M")
    except ValueError:
        print("Time must be in HHMM format")
        return get_time()
    else:
        return return_time


def get_course():
    courses = {
        "SC1003": "Introduction to Computational Thinking & Programming",
        "SC1004": "Linear Algebra for Computing",
        "SC1005": "Digital Logic",
        "SC1013": "Physics For Computing",
        "EG1001": "Engineers in Society",
        "CC0003": "Ethics & Civics in a Multicultural World",
        "CC0005": "Healthy Living & Wellbeing",
    }
    code = input("Course Code: ")
    try:
        code = code.upper()
        name = courses[code]
    except KeyError:
        print(
            f"{code} is not a valid course code\nAvailable courses: {", ".join(courses.keys())}"
        )
        get_course()
    return code, name


def get_type():
    lesson_types = {"lec": "lecture", "tut": "tutorial", "lab": "lab"}
    lesson_type = input("Type (Lecture, Tutorial, Lab): ").lower()
    if lesson_type in lesson_types:
        return lesson_types[lesson_type].title()
    elif lesson_type in lesson_types.values():
        return lesson_type.title()
    else:
        print(
            f"{lesson_type} is not a valid type\nAvailable types: {", ".join(lesson_types.keys())}"
        )
        get_type()
