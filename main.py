import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tournage

def afficher_type_usinage(fenetre):
    type_usinage_frame = tk.Frame(fenetre)
    type_usinage_frame.pack(pady=20)

    type_usinage = ["Fraisage", "Tournage", "Percage", "Taraudage", "Alésage"]
    combobox_usinage = ttk.Combobox(type_usinage_frame, values=type_usinage)
    combobox_usinage.set(type_usinage[0])
    combobox_usinage.pack(pady=10)

    def on_button_click():
        selected_usinage = combobox_usinage.get()
        if selected_usinage == "Fraisage":
            messagebox.showinfo("Information", f"Vous avez sélectionné {selected_usinage}. Cette option n'est pas encore implémentée")
        elif selected_usinage == "Tournage":
            tournage.afficher_materiaux(fenetre, type_usinage_frame, selected_usinage)  # Ajout de selected_usinage
        elif selected_usinage == "Percage":
            messagebox.showinfo("Information", f"Vous avez sélectionné {selected_usinage}. Cette option n'est pas encore implémentée")
        elif selected_usinage == "Taraudage":
            messagebox.showinfo("Information", f"Vous avez sélectionné {selected_usinage}. Cette option n'est pas encore implémentée")
        elif selected_usinage == "Alésage":
            messagebox.showinfo("Information", f"Vous avez sélectionné {selected_usinage}. Cette option n'est pas encore implémentée")

    button_suivant = tk.Button(type_usinage_frame, text="Suivant", command=on_button_click)
    button_suivant.pack()

# Fenetre principale
main_fenetre = tk.Tk()
main_fenetre.title("Sélection avec Listes Déroulantes")
main_fenetre.geometry("500x300")

afficher_type_usinage(main_fenetre)

main_fenetre.mainloop()

