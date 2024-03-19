import tkinter as tk
from tkinter import ttk
from classes import *


def add_product():
    # Cria uma nova janela Toplevel (pop-up)
    popup = tk.Toplevel(window)
    popup.geometry("500x500")
    popup.title("Adicionar produto")

    name = tk.StringVar()
    description = tk.StringVar()
    price = tk.DoubleVar()
    available = tk.BooleanVar()

    label_name = ttk.Label(popup, text="Nome:")
    label_name.grid(row=0, column=0, padx=10, pady=10)
    entry_name = ttk.Entry(popup, textvariable=name)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_description = ttk.Label(popup, text="Descrição:")
    label_description.grid(row=1, column=0, padx=10, pady=10)
    entry_description = ttk.Entry(popup, textvariable=description)
    entry_description.grid(row=1, column=1, padx=10, pady=10)

    label_price = ttk.Label(popup, text="Preço:")
    label_price.grid(row=2, column=0, padx=10, pady=10)
    entry_price = ttk.Entry(popup, textvariable=price)
    entry_price.grid(row=2, column=1, padx=10, pady=10)

    label_available = ttk.Label(popup, text="Disponível:")
    label_available.grid(row=3, column=0, padx=10, pady=10)
    entry_available = ttk.Checkbutton(popup,variable=available)
    entry_available.grid(row=3, column=1, padx=10, pady=10)

    # button_test = ttk.Button(popup, text="teste", command=lambda: print(p_name.get()))
    # button_test.pack()

    button_close = ttk.Button(popup, text="Fechar", command=popup.destroy)
    button_close.pack(side=tk.BOTTOM, padx=10, pady=10)



# window
window = tk.Tk()
window.geometry('600x400')
window.title('Produtos')

# data
product_list = ProductList()

button_add = ttk.Button(window, text="Adicionar produto", command=add_product)
button_add.pack(padx=20, pady=20)

# table
table = ttk.Treeview(window, columns=('p', 'price'), show='headings')
table.heading('p', text="Produto")
table.heading('price', text="Preço")
table.pack(fill='both', expand=True)

# insert values in treeview
for product in product_list.products:
    table.insert('', 'end', values=(product.name, product.price))

# run
window.mainloop()
