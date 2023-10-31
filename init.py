from operaciones import multi
def game():
    score = 0
    while True:
        print('========Menu========'
              '\n1.multiplicación'
              '\n0.Exit')
        option = int(input('\nChoice an option:')) 
        if option == 0:
            break
        num_1=input('Enterfirstnumber:')
        num_2=input('Entersecondnumber:')
        answer=int(input('Enteryouanswer:'))

        if option==1: 
            result = num_1 * num_2
            if result == answer:
                score+=2
                print('Correct!!')
            else:
                print('Incorrect')

            print(f'========GameOver========'
            f'\nYouscoreis{score}'
            '\nKeepgoing!')
            game()