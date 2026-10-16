from config import GRADE_A_LIMIT, GRADE_B_LIMIT, GRADE_C_LIMIT, GRADE_D_LIMIT

def calculate_grade(score):
    """ bala əsasən hərfi qiyməti hesablayır """
    if score >= GRADE_A_LIMIT:
        return "A"
    elif score >= GRADE_B_LIMIT:
        return "B"
    elif score >= GRADE_C_LIMIT:
        return "C"
    elif score >= GRADE_D_LIMIT:
        return "D"
    else:
        return "F"

def calculate_statistics(students):
    """ Ümumi statistik məlumatları hesablayır """
    if not students:
        return {
            "total_students": 0,
            "average_score": 0.0,
            "highest_score": 0,
            "lowest_score": 0
        }
    
    scores = [s["Score"] for s in students]
    return {
        "total_students": len(students),
        "average_score": round(sum(scores) / len(scores), 1),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }