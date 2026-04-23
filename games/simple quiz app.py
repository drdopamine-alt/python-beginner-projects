#store data
questions = {'What is 2*2 ?':'4','what is the capital of India?':'Delhi','what is the color of water?':'Blue'}
# initialize score to 0
score = 0
#For asking questions
for question in questions:
    answer = input(question)
    if answer == questions[question]:
        print('Correct!')
        score += 1
    else:
        print('Wrong answer')
print(score,'/',len(questions))