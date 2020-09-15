while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >=1 and opção <5:
        n = int(input("Tabuada de:"))
        i = 1
        while i<=10:
            if opção == 1:
                print("%d + %d = %d" % (n, i, n + i))
            elif opção == 2:
                print("%d - %d = %d" % (n, i, n - i))
            elif opção == 3:
                print("%d / %d = %5.4f" % (n, i, n / i))
            elif opção == 4:
                print("%d x %d = %d" % (n, i, n * i))
            i += 1
    else:
        print("Opção inválida!")
        