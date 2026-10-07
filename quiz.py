name = input("Wetin be your name: ")
score = 0

questions = [
  ("Drinking clean water prevents wetin?", "cholera"),
  ("Exercise good for wetin?", "health"),
  ("Which food gives vitamin A?", "carrot")
]

for q, correct in questions:
    ans = input(q + " ").lower()
    if correct in ans:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Na {correct} be answer")

print(f"\n{name}, you score {score}/{len(questions)}")
