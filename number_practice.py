from random import randint, seed

UNITS = ['Sıfır', 'Bir', 'İki', 'Üç', 'Dört', 'Beş', 'Altı', 'Yedi', 'Sekiz', 'Dokuz']
TENS = dict([(10, 'On'), (20, 'Yirmi'), (30, 'Otuz'), (40, 'Kırk'), (50, 'Elli'), (60, 'Atmış'), (70, 'Yetmiş'), (80, 'Seksen'), (90, 'Doksan'), (100, 'Yüz')])

def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

def get_num_str(num):
    pos_nums = get_pos_nums(num)
    num_str = ''
    while len(pos_nums) > 0:
        idx = pos_nums[-1]
        if idx != 0:
            try:
                if len(pos_nums) == 4:
                    num_str = '{} Bin '.format(UNITS[idx])
                elif len(pos_nums) == 3:
                    if idx == 1:
                        num_str = '{}Yüz '.format(num_str)
                    else:
                        num_str = '{}{} Yüz '.format(num_str, UNITS[idx])
                elif len(pos_nums) == 2:
                    num_str = '{}{} '.format(num_str, TENS[idx * 10])
                elif idx > 0:
                    num_str = '{}{} '.format(num_str, UNITS[idx])
            except:
                pass

        pos_nums.pop()

    return num_str

def do_test(lower_bound, upper_bound, num, correct_answer):
    msg = get_num_str(num)

    if not correct_answer :
        msg = 'Wrong answer, try again.\n{0}'.format(msg)

    ans = input(msg).strip()
    if ans == 'q':
        exit()
    ans = int(ans)
    return check_answer(num, ans)

def check_answer(num, ans):
    return num == ans

def main():
    seed()
    stop = False
    choice = int(input('What do you want to test? (0) Units, (1) Tens, (2) Everything\n').strip())
    upper_bound = 10000 if choice == 2 else 10 if choice == 1 else 9
    lower_bound = 1 if choice == 1 else 0
    mult = 10 if choice == 1 else 1

    while True:
        num = randint(lower_bound, upper_bound) * mult
        if num > 0:
            correct_answer = True
            while not do_test(lower_bound, upper_bound, num,  correct_answer):
                correct_answer = False

main()