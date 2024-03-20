import tkinter as tk
from tkinter import ttk
from classes import *


def popup_add_product():
    popup = tk.Toplevel(window)
    popup.geometry("500x500")
    popup.title("Adicionar produto")

    p_name = tk.StringVar()
    p_description = tk.StringVar()
    p_price = tk.DoubleVar()
    p_available = tk.BooleanVar()

    label_name = ttk.Label(popup, text="Nome:")
    label_name.grid(row=0, column=0, padx=10, pady=10)
    entry_name = ttk.Entry(popup, textvariable=p_name)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_description = ttk.Label(popup, text="Descrição:")
    label_description.grid(row=1, column=0, padx=10, pady=10)
    entry_description = ttk.Entry(popup, textvariable=p_description)
    entry_description.grid(row=1, column=1, padx=10, pady=10)

    label_price = ttk.Label(popup, text="Preço:")
    label_price.grid(row=2, column=0, padx=10, pady=10)
    entry_price = ttk.Entry(popup, textvariable=p_price)
    entry_price.grid(row=2, column=1, padx=10, pady=10)

    label_available = ttk.Label(popup, text="Disponível:")
    label_available.grid(row=3, column=0, padx=10, pady=10)
    entry_available = ttk.Checkbutton(popup, variable=p_available)
    entry_available.grid(row=3, column=1, padx=10, pady=10)

    def button_adicionar():
        p = Product(name=p_name.get(), description=p_description.get(),
                    price=float(p_price.get()), available=bool(p_available.get()))

        product_list.add_product(p)
        update_treeview()

        popup.destroy()

    button_popup_add = ttk.Button(popup, text="Adicionar", command=lambda: button_adicionar)
    button_popup_add.grid(row=4, column=0)


def update_treeview():
    for row in table.get_children():
        table.delete(row)

    for product in product_list.products:
        table.insert('', 'end', values=(product.name, product.price))


# window
window = tk.Tk()
window.geometry('600x400')
window.title('Produtos')

# data
product_list = ProductList()

button_add = ttk.Button(window, text="Adicionar produto", command=popup_add_product)
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
