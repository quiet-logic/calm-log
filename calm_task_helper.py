import random

def random_encouragement() -> str:
    messages = [
        "One quiet step at a time.",
        "Consistency > intensity.",
        "Gentle progress is real progress 🕯️",
        "You don't have to rush. You're building a life, not a sprint.",
        "Every little step is a win, no matter how small they seem.",
    ]
    return random.choice(messages)


def tiny_step(task: str) -> str:
    return f"Try just 5 minutes on: {task}"

task = input("What would you like to work on today? ")

print(tiny_step(task))
print(random_encouragement())

