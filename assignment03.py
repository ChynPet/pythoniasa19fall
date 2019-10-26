import random

def task1():
    """
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
    on a single line.
    """
    return ','.join( str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5)


def task2(rows, cols):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
    Example:
    Suppose the following inputs are given to the program: 3, 5.
    Then, the output of the program should be:
    >>> task2(3, 5)
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    return [[i*j for j in range(cols)] for i in range(rows)]


def task3(password):
    """
    A website requires the users to input username and password to register.
    Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
    Your program should accept a password and will check them according to the above criteria.
    Example:
    If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    >>> task3('ABd1234@1')
    True
    >>> task3('a F1#')
    False
    >>> task3('2w3E*')
    False
    >>> task3('2We3345')
    False
    """
    return True if 6 <= len(password) <= 12\
                and any('a' <= s <= 'z' for s in password)\
                and any('A' <= s <= 'Z' for s in password)\
                and any('0' <= s <= '9' for s in password)\
                and any(s in '#$@' for s in password) else False

def task4():
    """
    Write password generator function that uses the same rules as in Task 3.
    The password generator function must be able to generate all possible correct passwords.
    >>> task3(task4())
    True
    """
    #Alphabet on password
    lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_alphabet = [i.upper() for i in lower_alphabet]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['#','$','@']
    n = random.randint(6,12)
    #Function for generetion password
    def gen_pass(n_low_alp, n_upp_alp, n_num, n_sym):
        tmp = []
        for i in range (n_low_alp):
            tmp.append(random.choice(lower_alphabet))
        for i in range (n_upp_alp):
            tmp.append(random.choice(upper_alphabet))
        for i in range (n_num):
            tmp.append(random.choice(numbers))
        for i in range (n_sym):
            tmp.append(random.choice(symbols))
        #sort
        for k in range(n//2):
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            tmp[i], tmp[j] = tmp[j], tmp[i]
        return ''.join(i for i in tmp)
    
    if 6 <= n <= 7:
        #Count symbols
        n_low_alp = random.randint(1,2)
        n_upp_alp = random.randint(1,2)
        n_num = 1
        n_sym = 1
        #Check
        if n_low_alp + n_upp_alp + n_num + n_sym == n:
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
        else:
            how_to_add = random.randint(1,4)
            if how_to_add == 1:
                n_low_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 2:
                n_upp_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 3:
                n_num += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 4:
                n_sym += n - n_low_alp - n_upp_alp - n_num - n_sym
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
    elif 8 <= n <= 9:
        #Count symbols
        n_low_alp = random.randint(1,2)
        n_upp_alp = random.randint(1,2)
        n_num = random.randint(1,2)
        n_sym = random.randint(1,2)
        #Check
        if n_low_alp + n_upp_alp + n_num + n_sym == n:
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
        else:
            how_to_add = random.randint(1,4)
            if how_to_add == 1:
                n_low_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 2:
                n_upp_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 3:
                n_num += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 4:
                n_sym += n - n_low_alp - n_upp_alp - n_num - n_sym
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)     
    elif 10 <= n <= 11:
        #Count symbols
        n_low_alp = random.randint(1,3)
        n_upp_alp = random.randint(1,3)
        n_num = random.randint(1,2)
        n_sym = random.randint(1,2)
        #Check
        if n_low_alp + n_upp_alp + n_num + n_sym == n:
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
        else:
            how_to_add = random.randint(1,4)
            if how_to_add == 1:
                n_low_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 2:
                n_upp_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 3:
                n_num += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 4:
                n_sym += n - n_low_alp - n_upp_alp - n_num - n_sym
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
    elif n == 12:
        #Count symbols
        n_low_alp = random.randint(1,3)
        n_upp_alp = random.randint(1,3)
        n_num = random.randint(1,3)
        n_sym = random.randint(1,3)
        #Check
        if n_low_alp + n_upp_alp + n_num + n_sym == n:
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)
        else:
            how_to_add = random.randint(1,4)
            if how_to_add == 1:
                n_low_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 2:
                n_upp_alp += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 3:
                n_num += n - n_low_alp - n_upp_alp - n_num - n_sym
            elif how_to_add == 4:
                n_sym += n - n_low_alp - n_upp_alp - n_num - n_sym
            return gen_pass(n_low_alp, n_upp_alp, n_num, n_sym)

if __name__ == '__main__':
    import doctest
    doctest.testmod()