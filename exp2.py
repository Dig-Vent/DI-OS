import pygetwindow as gw

# Listar todas as janelas abertas no sistema
a = gw.getActiveWindow()
windows = gw.getAllTitles()
#print(windows)
print(a)

# Filtrar as janelas que têm título visível
visible_windows = [w for w in windows if w.strip()]

print("Janelas abertas no sistema:")
for i, window in enumerate(visible_windows, 1):
    print(f"{i}. {window}")

if __name__ == "__main__":
    pass
