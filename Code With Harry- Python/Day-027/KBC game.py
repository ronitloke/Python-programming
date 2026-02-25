print("Chaliye Let's play kaun banega crorepati\n")
print("Pehla sawaal apki screen par ye raha\n")
def func1(options):
    l1=["Q1: The International Literacy Day is observed on?"]
    print(l1)
    print()
    print("your options are as follows:\n")
    print("a:Sept 8")
    print("b:Nov 28")
    print("c:May 2")
    print("d:Sep 22\n")

    match options:

        case  'a':
            print("Sep 8")
        case 'b':
            print("Nov 28")
        case 'c':
            print("May 2")
        case 'd':
            print("Sep 22")
        case 'e':
            print("All the best!!!")
        case _:
            print("Invalid input")
    print()

    Ans = input("Enter Your answer:\n")

    if Ans == 'a':
        print("You won 1,000\n")
    else:
        print("Ye uttar galat hai.. sahi jawab hai a:Sept 8\n")
        print("Game over\n")


print(func1('e'))

print("Dusra sawaal apki screen par ye raha\n")
def func2(options):
    l2 = ["Q2: The language of Lakshadweep. a Union Territory of India, is?"]
    print(l2)
    print()
    print("your options are as follows:\n")
    print("a:Tamil")
    print("b:Hindi")
    print("c:Malayalam")
    print("d:Telugu\n")

    match options:

        case  'a':
            print("Tamil")
        case 'b':
            print("Hindi")
        case 'c':
            print("Malayalam")
        case 'd':
            print("Telugu")
        case 'e':
            print("All the best!!!")
        case _:
            print("Invalid input")
    print()

    Ans = input("Enter Your answer:\n")

    if Ans == 'c':
        print("You won 2,000\n")
    else:
        print("Ye uttar galat hai.. sahi jawab hai c:Malayalam\n")
        print("Game over\n")
print(func2('e'))


print("Tisra sawaal apki screen par ye raha\n")
def func3(options):
    l3 = ["Q3: In which group of places the Kumbha Mela is held every twelve years?"]
    print(l3)
    print()
    print("your options are as follows:\n")
    print("a:Ujjain. Purl; Prayag. Haridwar")
    print("b:Prayag. Haridwar, Ujjain,. Nasik")
    print("c:Rameshwaram. Purl, Badrinath. Dwarika")
    print("d:Chittakoot, Ujjain, Prayag,'Haridwar\n")

    match options:

        case  'a':
            print("Ujjain. Purl; Prayag. Haridwar")
        case 'b':
            print("Prayag. Haridwar, Ujjain,. Nasik")
        case 'c':
            print("Rameshwaram. Purl, Badrinath. Dwarika")
        case 'd':
            print("Chittakoot, Ujjain, Prayag,'Haridwar")
        case 'e':
            print("All the best!!!")
        case _:
            print("Invalid input")
    print()

    Ans = input("Enter Your answer:\n")

    if Ans == 'b':
        print("You won 3,000\n")
    else:
        print("Ye uttar galat hai.. sahi jawab hai b:Prayag. Haridwar, Ujjain,. Nasik\n")
        print("Game over\n")
print(func3('e'))


print("Chauta sawaal apki screen par ye raha\n")
def func4(options):
    l4 = ["Q4: Bahubali festival is related to?"]
    print(l4)
    print()
    print("your options are as follows:\n")
    print("a:Islam")
    print("b:Hinduism")
    print("c:Buddhism")
    print("d:Jainism\n")

    match options:

        case  'a':
            print("Islam")
        case 'b':
            print("Hinduism")
        case 'c':
            print("Buddhism")
        case 'd':
            print("Jainism")
        case 'e':
            print("All the best!!!")
        case _:
            print("Invalid input")
    print()

    Ans = input("Enter Your answer:\n")

    if Ans == 'd':
        print("You won 4,000\n")
    else:
        print("Ye uttar galat hai.. sahi jawab hai d:Jainism\n")
        print("Game over\n")
print(func4('e'))


print("Pachva sawaal apki screen par ye raha\n")
def func5(options):
    l5 = ["Q5: Which day is observed as the World Standards  Day?"]
    print(l5)
    print()
    print("your options are as follows:\n")
    print("a:June 26")
    print("b:Oct 14")
    print("c:Nov 15")
    print("d:Dec 2\n")

    match options:

        case  'a':
            print("June 26")
        case 'b':
            print("Oct 14")
        case 'c':
            print("Nov 15")
        case 'd':
            print("Dec 2")
        case 'e':
            print("All the best!!!")
        case _:
            print("Invalid input")
    print()

    Ans = input("Enter Your answer:\n")

    if Ans == 'd':
        print("You won 5,000\n")
    else:
        print("Ye uttar galat hai.. sahi jawab hai b:Oct 14\n")
        print("Game over\n")
print(func5('e'))

