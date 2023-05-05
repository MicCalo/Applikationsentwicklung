data = [[1, 'Max', 'Muster'], [2, 'Anita', 'Breitenmoser'], [15, 'Theobald', 'Willibald'], [233, 'Kunigunde', 'Meier'], [5, 'Anton', 'Andres']]
column_widths=[5, 20, 20]


print("{:<{width1}} {:<{width2}} {:<{width3}}".format('ID', 'Vorname', 'Nachname', width1=column_widths[0], width2=column_widths[1], width3=column_widths[2]))

for info in data:
    ID, Vorname, Nachname = info
    print("{:<{width1}} {:<{width2}} {:<{width3}}".format(ID, Vorname, Nachname, width1=column_widths[0], width2=column_widths[1], width3=column_widths[2]))
