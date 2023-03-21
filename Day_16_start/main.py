from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirrel", "Charmander"])
table.add_column("Type", ["Electric", "Water", "fire"])
table.align = 'l'

print(table)