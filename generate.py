import random

def generateHTML(content):
    with open("mathbase.html", "r") as f:
        template = f.read()
    for i in content:
        template = template + f"<p>{i}</p>\n"
    with open("index.html", "w") as file:
        file.write(template)

def generateMath():
    operatorsEasy = ["+", "-"]
    operatorsHard = ["*", ":"]
    mathContent = []
    for i in range(15):
        op = random.choice(operatorsEasy)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        mathContent.append(f"{num1} {op} {num2} = ")
    for i in range(15):
        op = random.choice(operatorsHard)
        num1 = random.randint(1, 10)
        if op == ":":
            num2 = num1 * random.randint(0,10)
            num1, num2 = num2, num1
        else:
            num2 = random.randint(1, 10)
        mathContent.append(f"{num1} {op} {num2} = ")
    return mathContent

    print(mathContent)

content = generateMath()
generateHTML(content)