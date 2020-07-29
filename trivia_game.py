print('Hello, Welcome to Trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 5

if ans.lower() == 'yes':
    ans = input('1. What is the best programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('2. What is the capital of Colombia? ')
    if ans.lower() == 'bogota':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. What index do Arrays start at? ')
    if ans == '0':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('4. Who wrote "For Whom the Bell Tolls?" ')
    if ans.lower() == 'ernest hemingway' or ans.lower() == 'hemingway':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('5. Who cheated to win their world series? ')
    if ans.lower() == 'astros' or ans.lower() == 'the astros':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

print('thank you for playing, you got {} questions correct.'.format(score))
mark = (score/total_q) * 100

print('Mark: {}'.format(mark))
print('Goodbye')

    



    