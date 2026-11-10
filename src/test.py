from lark import Lark

parser = Lark(open("src/gramatica.lark", encoding="utf-8").read(), parser="lalr")
texto = open("modelos/life.ca", encoding="utf-8").read()
arbol = parser.parse(texto)
print(arbol.pretty())