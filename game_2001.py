from random import randint


def game_2001():
    """
    Game where user and computer throw dices. That player win, who first will have 2001 points.
    :return: User and computer score.
    """
    user_score = 0
    computer_score = 0
    user_throws = []
    computer_throws = []
    turn_count = 0  # zmienna do śledzenia tury rozgrywki

    while user_score <= 2001 and computer_score <= 2001:
        info = input('Press Enter to start turn: ')
        u_turn_score = 0  # zmienna do przeniesienia wyniku rzutów tylko z danej tury do zmiennej user_throws
        c_turn_score = 0  # zmienna do przeniesienia wyniku rzutów tylko z danej tury do zmiennej computer_throws
        for _ in range(2):
            one_throw = randint(1, 6)
            u_turn_score += one_throw  # dodanie do siebie dwóch pojedynczych rzutów kostką
            # print(one_throw)
            c_one_throw = randint(1, 6)
            c_turn_score += c_one_throw  # dodanie do siebie dwóch pojedynczych rzutów kostką
            # print(c_one_throw)
        user_throws.append(u_turn_score)  # dodanie konkretnego wyniku do zmiennej user_throws
        print(f'Rzuty użytkownika w poszczególnych turach: {user_throws}')

        computer_throws.append(c_turn_score)  # dodanie konkretnego wyniku do zmiennej computer_throws
        print(f'Rzuty komputera w poszczególnych turach: {computer_throws}')

        if turn_count >= 1:  # warunek, aby rozpocząć dodatkowe wyjątki od drugiej tury
            if u_turn_score == 7:  # warunki specjalne
                user_score = user_score // 7

            elif u_turn_score == 11:
                user_score = user_score * 11
            else:
                user_score += u_turn_score

        else:
            user_score += u_turn_score
        print(f' Aktualny wynik gracza po bieżącej turze to: {user_score}')
        if turn_count >= 1:  # warunek, aby rozpocząć dodatkowe wyjątki od drugiej tury
            if c_turn_score == 7:  # warunki specjalne
                computer_score = computer_score // 7

            elif c_turn_score == 11:
                computer_score = computer_score * 11
            else:
                computer_score += c_turn_score

        else:
            computer_score += c_turn_score

        print(f' Aktualny wynik komputera po bieżącej turze to: {computer_score}')
        turn_count += 1  # zwiększenie licznika tury

    return user_score


score = game_2001()
print(score)
