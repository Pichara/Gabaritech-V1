from defs import choices, linha, color, find_answer_in_string
from time import sleep
import time
import os
from fractions import Fraction

while True:
    linha()
    print(color("""GABARITECH""", "Blue").center(69))
    print("""Which test mode do you want??
(1) - ENEM
(2) - SAT 
(3) - Timer """) 
    linha()
    chosen1 = choices(3)

    #MODELO ENEM
    if chosen1 == 1: 
        while True:
            linha()
            print(color("""MODELO ENEM""", "Blue").center(69))
            print("What do you wanna do??")
            print("""(1) - See the test answers
(2) - Create a new test answer
(3) - Check the results
(4) - Back""")
            linha()
            chosen2 = choices(4)
            if chosen2 == 1:  #See all the test anwers
                linha()
                #Checking how many test answers saves have
                with open("contadorENEM.txt", "r") as data:
                    cont = data.readlines()
                if cont[0] == "1":
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:   
                    print("Do you want see the result of which test??")
                    for i in range(int(cont[0]) - 1):
                        print(f"{i+1} - 'Data_Enem_{i+1}'")
                    test_choice = choices(int(cont[0])- 1)

                #Showing the gabarito
                while True:
                    linha()
                    with open(f"Data_Enem_{test_choice}.txt", "r") as data:
                        lines = data.readlines()
                        for line in lines:
                            print(line)
                    print("""\n
(1) - Repair
(2) - Continue\n""")
                    chosen4 = choices(2)
                    if chosen4 == 1: #Repair the test answer
                        verifier = 0
                        while True: #Tratamento de erro
                            try:
                                error_line = int(input("(?): "))
                                error_line = str(error_line)
                            except:
                                print(color("Please, only numbers!!", "Red"))
                                sleep(1)
                                continue
                            with open(f"Data_Enem_{test_choice}.txt", "r") as data:
                                lines = data.readlines()
                                for i in range(len(lines)):
                                    if error_line in lines[i]:
                                        lines[i] = (f"({i+1}) = {input(f'({i+1}) = ')}\n")
                                        verifier = 1
                                if verifier == 0:
                                    print(color("Error: error_line not found", "Red"))
                                    continue
                                else:
                                    break  
                             
                        with open(f"Data_Enem_{test_choice}.txt", "w") as data:
                            for line in lines:
                                data.write(line)                     
                    if chosen4 == 2:
                        break
            elif chosen2 == 2: #Save test gabarito in data
                linha()
                results = []
                #Checking how many tests saves have and regulating this with +1
                with open("contadorENEM.txt", "r") as file:
                    cont = file.readlines()
                    with open("contadorENEM.txt", "w") as file:
                        file.write(f"{int(cont[0]) + 1}")    
                #Inputing the gabarito of the test
                for i in range(5):
                    while True:
                        library = {f"({i+1})": str(input(f"Question {i+1}: ")).upper()}
                        if library[f"({i+1})"] == "A" or library[f"({i+1})"] == "B" or library[f"({i+1})"] == "C" or library[f"({i+1})"] == "D" or library[f"({i+1})"] == "E":
                            results.append(library)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D or E", "Red").center(69))
                            continue
                #Saving the data
                with open(f"Data_Enem_{cont[0]}.txt", "w") as data:
                    for line in results:
                        for k,v in line.items():
                            data.write(f"{k} = {v}\n")
                continue
            elif chosen2 == 3: #Check the results with the test in data
                linha()
                results = []
                #Checking how many tests saves have
                with open("contadorENEM.txt", "r") as data:
                    cont = data.readlines()
                if cont[0] == "1":
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:
                    print("Do you wanna check the results of which test??")
                    for i in range(int(cont[0]) - 1):
                        print(f"{i+1} - 'Data_Enem_{i+1}'")
                test_choice = choices(int(cont[0]) - 1)
                #Inputing the results of the test
                for i in range(5):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                linha()
                sleep(1)
                print("$ = Correct\nX = Wrong\n\n")
                sleep(2)
                #Colecting the gabarito as a list
                with open(f"Data_Enem_{test_choice}.txt", "r+") as data:
                    gabarito = data.readlines() #Respostas | if marcadas == respostas: (correct)
                for i in range(5):
                    if results[i] in gabarito[i]:
                        print(f"({i+1}) = {results[i]} - {color('$', 'Green')}")
                    else:
                        print(f"({i+1}) = {results[i]} - {color('X', 'Red')} [{find_answer_in_string(gabarito[i])}]")
                linha()
                sleep(4)
                break
            elif chosen2 == 4: #back
                break
    #MODELO SAT
    elif chosen1 == 2:
        while True:
            linha()
            print(color("""MODELO SAT""", "Blue").center(69))
            print("What do you wanna do??")
            print("""(1) - See the test answers 
(2) - Create a new test answer
(3) - Check the results
(4) - Back""")
            linha()
            chosen3 = choices(4)
            if chosen3 == 1: #See all test answers
                linha()
                #Checking how many test answers saves have
                with open("contadorSAT.txt", "r") as data:
                    cont = data.readlines()
                if cont[0] == "1":
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:   
                    print("Do you want see the result of which test??")
                    for i in range(int(cont[0]) - 1):
                        print(f"{i+1} - 'Data_SAT_{i+1}'")
                    test_choice = choices(int(cont[0])- 1)

                #Showing the gabarito
                while True:
                    linha()
                    with open(f"Data_SAT_{test_choice}.txt", "r") as data:
                        lines = data.readlines()
                        for line in lines:
                            print(line)
                        print("""\n
(1) - Repair
(2) - Continue\n""")
                        chosen4 = choices(2)
                        if chosen4 == 1: #Repair the test answer
                            verifier = 0
                            while True: #Tratamento de erro
                                R = 1
                                W = 1
                                M = 1
                                Mc = 1
                                try:
                                    print("""In what section are the error:
1 - Reading
2 - Writing
3 - Math
4 - MathC\n""")
                                    chosen5 = choices(4)
                                    error_line = int(input("(?): "))
                                    error_line = (f"({error_line})")
                                except:
                                    print(color("Please, only numbers!!", "Red"))
                                    sleep(1)
                                    continue
                                with open(f"Data_SAT_{test_choice}.txt", "r") as data:
                                    lines = data.readlines()
                                    for i in range(len(lines)):
                                        if chosen5 == 1:
                                            if i < 53:
                                                if error_line in lines[i]:
                                                    lines[i] = (f"({R}) = {input(f'({R}) = ')}\n")
                                                    verifier = 1
                                                R += 1
                                        elif chosen5 == 2:
                                            if i > 53 and i < 98:
                                                if error_line in lines[i]:
                                                    lines[i] = (f"({W}) = {input(f'({W}) = ')}\n")
                                                    verifier = 1
                                                W += 1
                                        elif chosen5 == 3:
                                            if i > 98 and i < 119:
                                                if error_line in lines[i]:
                                                    lines[i] = (f"({M}) = {input(f'({M}) = ')}\n")
                                                    verifier = 1
                                                M += 1
                                        elif chosen5 == 4:
                                            if i > 119:
                                                if error_line in lines[i]:
                                                    lines[i] = (f"({Mc}) = {input(f'({Mc}) = ')}\n")
                                                    verifier = 1
                                                Mc += 1

                                    if verifier == 0:
                                        print(color("Error: error_line not found", "Red"))
                                        continue
                                    else:
                                        break  
                            with open(f"Data_SAT_{test_choice}.txt", "w") as data:
                                for line in lines:
                                    data.write(line)     
                        if chosen4 == 2:
                            break

            if chosen3 == 2: #Save a test answers
                linha()
                reading = []
                writing = []
                math = []
                mathC = []
                #Checking how many tests saves have and regulating this with +1
                with open("contadorSAT.txt", "r") as file:
                    cont = file.readlines()
                    with open("contadorSAT.txt", "w") as file:
                        file.write(f"{int(cont[0]) + 1}")    
                #Inputing the gabarito of the test
                print(color("READING", "Yellow").center(69))
                for i in range(52):
                    while True:
                        library = {f"({i+1})": str(input(f"Question {i+1}: ")).upper()}
                        if library[f"({i+1})"] == "A" or library[f"({i+1})"] == "B" or library[f"({i+1})"] == "C" or library[f"({i+1})"] == "D":
                            reading.append(library)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D", "Red").center(69))
                            continue
                print(color("WRITING", "Yellow").center(69))
                for i in range(44):
                    while True:
                        library = {f"({i+1})": str(input(f"Question {i+1}: ")).upper()}
                        if library[f"({i+1})"] == "A" or library[f"({i+1})"] == "B" or library[f"({i+1})"] == "C" or library[f"({i+1})"] == "D":
                            writing.append(library)
                            break
                        else:
                            print(color("Please, only choice A, B, C, D", "Red").center(69))
                            continue
                print(color("MATH", "Yellow").center(69))
                for i in range(20):
                    if i < 15:
                        while True:
                            library = {f"({i+1})": str(input(f"Question {i+1}: ")).upper()}
                            if library[f"({i+1})"] == "A" or library[f"({i+1})"] == "B" or library[f"({i+1})"] == "C" or library[f"({i+1})"] == "D":
                                math.append(library)
                                break
                            else:
                                print(color("Please, only choice A, B, C, D", "Red").center(69))
                                continue
                    else:
                        while True: #Tratamento de erro para numeros float e fracionarios
                            try:
                                library = {f"({i+1})": float(Fraction(input(f"Question {i+1}: ")))}  
                                math.append(library)
                                break   
                            except:
                                try:
                                    library[f"({i+1})"] = float(Fraction(library[f"({i+1})"]))
                                    math.append(library)
                                    break
                                except:
                                    print(color("Please, only float and fractions numbers in this part of section!", "Red").center(69))        
                                    continue
                print(color("MATH - CALCULATOR", "Yellow").center(69))
                for i in range(38):
                    if i < 30:
                        while True:
                            library = {f"({i+1})": str(input(f"Question {i+1}: ")).upper()}
                            if library[f"({i+1})"] == "A" or library[f"({i+1})"] == "B" or library[f"({i+1})"] == "C" or library[f"({i+1})"] == "D":
                                mathC.append(library)
                                break
                            else:
                                print(color("Please, only choice A, B, C, D", "Red").center(69))
                                continue
                    else:
                        while True: #Tratamento de erro para numeros float e fracionarios
                            try:
                                library = {f"({i+1})": float(Fraction(input(f"Question {i+1}: ")))}  
                                mathC.append(library)
                                break   
                            except:
                                print(color("Please, only float and fractions numbers in this part of section!", "Red").center(69))        
                                continue

                #Saving the all the data
                with open(f"Data_SAT_{cont[0]}.txt", "w") as data:
                    data.write(color("READING\n", "Yellow"))
                    for line in reading:
                        for k,v in line.items():
                            data.write(f"{k} = {v}\n")
                    data.write(color("WRITING\n", "Yellow"))
                    for line in writing:
                        for k,v in line.items():
                            data.write(f"{k} = {v}\n")
                    data.write(color("MATH\n", "Yellow"))
                    for line in math:
                        for k,v in line.items():
                            data.write(f"{k} = {v}\n")
                    data.write(color("MATH - CALCULATOR\n", "Yellow"))
                    for line in mathC:
                        for k,v in line.items():
                            data.write(f"{k} = {v}\n")
            elif chosen3 == 3: #Check the results with the test in data
                linha()
                results = []
                #Checking how many tests saves have
                with open("contadorSAT.txt", "r") as data:
                    cont = data.readlines()
                if cont[0] == "1":
                    print(color("You did'nt save any test yet", "Red").center(69))
                    sleep(3)
                    continue
                else:
                    print("Do you wanna check the results of which test??")
                    for i in range(int(cont[0]) - 1):
                        print(f"{i+1} - 'Data_SAT_{i+1}'")
                test_choice = choices(int(cont[0]) - 1)
                #Inputing the results of the test
                print(color("READING", "Yellow").center(69))
                results.append("@")
                for i in range(52):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("WRITING", "Yellow").center(69))
                results.append("@")
                for i in range(44):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("MATH", "Yellow").center(69))
                results.append("@")
                for i in range(20):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                print(color("MATH - CALCULATOR", "Yellow").center(69))
                for i in range(38):
                    answer = input(f"Question({i+1}) = ")
                    results.append(answer)
                linha()
                sleep(1)
                print("$ = Correct\nX = Wrong\n\n")
                sleep(2)
                #Colecting the gabarito as a list
                with open(f"Data_SAT_{test_choice}.txt", "r+") as data:
                    gabarito = data.readlines() #Respostas | if marcadas == respostas: (correct)
                for i in range(157):
                    if i == 0:
                        print(color("READING", "Yellow").center(69))
                    elif i == 53:
                        print(color("WRITING", "Yellow").center(69))
                    elif i == 97:
                        print(color("MATH", "Yellow").center(69))
                    elif i == 119:
                        print(color("MATH - CALCULATOR", "Yellow").center(69))
                    elif results[i] in gabarito[i]:
                        print(f"({i+1}) = {results[i]} - {color('$', 'Green')}")
                    else:
                        print(f"({i+1}) = {results[i]} - {color('X', 'Red')} [{find_answer_in_string(gabarito[i])}]")
                linha()
                sleep(4)
                break
            elif chosen3 == 4: #back
                break
    #Timer
    elif chosen1 == 3:
        linha()
        print(color("SAT TIMER", "Blue").center(69))
        datas = []
        while True:
            start_time = 0
            true_break = False
            end_time = 0
            running = False
            
            while True:
                input_key = input("Press 'enter' to start/stop the timer and 'x' to finish!: ")
                if input_key == "x":
                    linha()
                    print(color("Avarege time", "Green").center(69))
                    print('\n')
                    total = 0
                    for data in datas:
                        print(data)
                        only_number = float(data.replace("Elapsed time: ", "").replace("seconds.", ""))
                        total += only_number
                    totaln = len(datas)
                    if totaln == 0:
                        totaln = 1
                    mean = total/totaln
                    print("\n")
                    print("Mean Time: {:.2f}".format(mean))
                    sleep(5)
                    true_break == True
                    break  
                
                else: 
                    if not running:
                        running = True
                        start_time = time.time()
                        print("Timer started.")
                    else:
                        running = False
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print("Timer stopped. Elapsed time: {:.2f} seconds.".format(elapsed_time))
                        datas.append("Elapsed time: {:.2f} seconds.".format(elapsed_time))
                        break
            if true_break:
                break
        