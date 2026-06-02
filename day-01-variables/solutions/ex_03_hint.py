"""Hints for ex_03

    name = input("Student name: ")
    subjects = []
    scores = []
    for i in range(3):
        s = input(f"Subject {i+1}: ")
        sc = float(input(f"  {s} score: "))
        subjects.append(s)
        scores.append(sc)

    avg = sum(scores) / len(scores)

    # Use if/elif to assign grade based on avg

    # Print report card with f-strings and alignment
    # e.g., print(f"{'Subject':<20}{'Score':<10}")
"""
