import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from math import pi

### Commun ###
def page_type_usinage(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un type d'usinage", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des types d'usinage
    types_usinage = ["Fraisage", "Tournage", "Percage", "Taraudage", "Alésage"]
    combobox_usinage = ttk.Combobox(fenetre, values=types_usinage)
    combobox_usinage.set(types_usinage[0])
    combobox_usinage.pack(pady=10)

    def on_button_click():
        type_usinage = combobox_usinage.get()
        if type_usinage == "Fraisage":
            changement_page(fenetre, fraisage, 1)
        elif type_usinage == "Tournage":
            changement_page(fenetre, tournage, 1)
        elif type_usinage == "Percage":
            changement_page(fenetre, percage, 1)
        elif type_usinage == "Taraudage":
            changement_page(fenetre, taraudage, 1)
        elif type_usinage == "Alésage":
            changement_page(fenetre, alesage, 1)
        else:
            messagebox.showinfo("Info", f"Le type d'usinage '{type_usinage}' n'est pas encore implémenté.")

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: on_button_click())
    bouton_suivant.pack(pady=20)

def page_materiaux(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un matériau", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des matériaux
    materiaux = ["Acier non allié (P)",
                 "Acier faiblement allié (P)",
                 "Acier fortement allié (P)",
                 "Acier moulé fortement allié (P)",
                 "Inox (M)",
                 "Fonte lamellaire (K)",
                 "Fonte modulaire (K)",
                 "Fonte sphéroïdale (K)",
                 "Aluminium faible dureté + silicium comme 2030 (N)",
                 "Aluminium forte dureté + silicium comme 6060(N)",
                 "Aluminium +12% de silicium (N)"
                 ]
    combobox_materiaux = ttk.Combobox(fenetre, values=materiaux)
    combobox_materiaux.set(materiaux[0])
    combobox_materiaux.pack(pady=10)

    global materiau
    materiau = combobox_materiaux.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def changement_page(fenetre, flux_pages, index):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    if index < len(flux_pages):
        flux_pages[index](fenetre, flux_pages, index)
    else:
        messagebox.showerror("Erreur", "Index de page invalide.")

### Fraisage ###
def page_operation_fraisage(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un type d'usinage", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des types d'usinage
    types_usinage_fraisage = ["Surfacage", "Rainurage", "Contournage", "Sciage", "Plongée verticale"]
    combobox_usinage_fraisage = ttk.Combobox(fenetre, values=types_usinage_fraisage)
    combobox_usinage_fraisage.set(types_usinage_fraisage[0])
    combobox_usinage_fraisage.pack(pady=10)

    global fraisage
    fraisage = combobox_usinage_fraisage.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def page_outil_fraisage(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner une nuance d'outil", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des outils
    outils = ["ARS lisse", "Carbure lisse", "ARS RAVA", "Carbure RAVA"]
    combobox_outil_fraisage = ttk.Combobox(fenetre, values=outils)
    combobox_outil_fraisage.set(outils[0])
    combobox_outil_fraisage.pack(pady=10)

    global outil
    outil = combobox_outil_fraisage.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def page_resultat_fraisage(fenetre):
    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiaux}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

### Tournage ###
def page_operation_tournage(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner une opération", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des opérations
    operations = ["Ebauche extérieure", "Ebauche intérieure", "Finition extérieure", "Finition intérieure", "Tronconnage", "Gorge", "Filetage"]
    combobox_operation_tournage = ttk.Combobox(fenetre, values=operations)
    combobox_operation_tournage.set(operations[0])
    combobox_operation_tournage.pack(pady=10)

    global operation
    operation = combobox_operation_tournage.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def page_outil_tournage(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner une nuance d'outil", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des outils
    outils = ["ARS", "Carbure"]
    combobox_outil_tournage = ttk.Combobox(fenetre, values=outils)
    combobox_outil_tournage.set(outils[0])
    combobox_outil_tournage.pack(pady=10)

    def on_button_click():
        page = combobox_outil_tournage.get()
        return page

    global outil
    outil = combobox_outil_tournage.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def page_rayon_bec(fenetre, flux_pages, index_page):

    # Titre de la page
    titre_rayon_bec = tk.Label(fenetre, text="Rayon de plaquette", font=("Arial", 16))
    titre_rayon_bec.pack(pady=20)

    # Frame pour les champs d'entrée
    rayon_bec_frame = tk.Frame(fenetre)
    rayon_bec_frame.pack(pady=20)

    label_rayon_bec = tk.Label(rayon_bec_frame, text="Entrez le rayon de la plaquette :")
    label_rayon_bec.pack(pady=5)

    entry_rayon_bec = tk.Entry(rayon_bec_frame)
    entry_rayon_bec.pack(pady=10)

    def on_button_click():
        try:
            global rayon
            rayon = float(entry_rayon_bec.get())
            if rayon > 0:
                # Si rayon valide, passer à la page suivante
                changement_page(fenetre, flux_pages, index_page + 1)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un rayon positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    # Bouton Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=on_button_click)
    bouton_suivant.pack(pady=20)

def page_diametre_piece(fenetre, flux_pages, index_page):
    # Titre de la page
    titre_diametre_piece = tk.Label(fenetre, text="Diamètre de la pièce", font=("Arial", 16))
    titre_diametre_piece.pack(pady=20)

    # Frame pour les champs d'entrée
    diametre_piece_frame = tk.Frame(fenetre)
    diametre_piece_frame.pack(pady=20)

    label_diametre_piece = tk.Label(diametre_piece_frame, text="Entrez le diamètre de la pièce :")
    label_diametre_piece.pack(pady=5)

    entry_diametre_piece = tk.Entry(diametre_piece_frame)
    entry_diametre_piece.pack(pady=10)

    def on_button_click():
        try:
            global diametre
            diametre = float(entry_diametre_piece.get())
            if diametre > 0:
                # Si rayon valide, passer à la page suivante
                changement_page(fenetre, flux_pages, index_page + 1)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un diametre positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    # Bouton Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=on_button_click)
    bouton_suivant.pack(pady=20)

def page_resultat_tournage(fenetre, flux_pages, index):
    # Calculs
    avance =55
    profondeur_passe= 66
    rotation =1000

    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiau}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

### Percage ###
def page_diametre_foret(fenetre, flux_pages, index_page):
    # Titre de la page
    titre_diametre_foret = tk.Label(fenetre, text="Diamètre du foret", font=("Arial", 16))
    titre_diametre_foret.pack(pady=20)

    # Frame pour les champs d'entrée
    diametre_foret_frame = tk.Frame(fenetre)
    diametre_foret_frame.pack(pady=20)

    label_diametre_foret = tk.Label(diametre_foret_frame, text="Entrez le diamètre du foret :")
    label_diametre_foret.pack(pady=5)

    entry_diametre_foret = tk.Entry(diametre_foret_frame)
    entry_diametre_foret.pack(pady=10)

    def on_button_click():
        try:
            global diametre
            diametre = float(entry_diametre_foret.get())
            if diametre > 0:
                # Si rayon valide, passer à la page suivante
                changement_page(fenetre, flux_pages, index_page + 1)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un diametre positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    # Bouton Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=on_button_click)
    bouton_suivant.pack(pady=20)

def page_resultat_foret(fenetre, flux_pages, index):
    # Calculs
    avance = 55
    profondeur_passe = 66
    rotation = 1000

    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiau}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

### Taraudage ###
def page_vis(fenetre, flux_pages, index_page):
    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un diamètre de vis", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des vis
    m_vis = ["M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20"]
    combobox_vis = ttk.Combobox(fenetre, values=m_vis)
    combobox_vis.set(m_vis[0])
    combobox_vis.pack(pady=10)

    global vis
    vis = combobox_vis.get()

    # Suivant
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changement_page(fenetre, flux_pages, index_page + 1))
    bouton_suivant.pack(pady=20)

def page_resultat_taraudage(fenetre, flux_pages, index):
    # Calculs
    avance =55
    profondeur_passe= 66
    rotation =1000

    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiau}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

### Alésage ###
def page_resultat_alesage(fenetre, flux_pages, index):
    # Calculs
    avance =55
    profondeur_passe= 66
    rotation =1000

    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiau}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

# Variables
materiau = ""
operation = ""
outil = ""
rayon = ""
diametre = ""
vis = ""

# Flux de page
fraisage = [page_type_usinage, page_materiaux, page_outil_fraisage, page_operation_fraisage, page_resultat_fraisage]
tournage = [page_type_usinage, page_materiaux, page_outil_tournage, page_operation_tournage, page_rayon_bec, page_diametre_piece, page_resultat_tournage]
percage = [page_type_usinage, page_materiaux, page_outil_tournage, page_diametre_foret, page_resultat_foret]
taraudage = [page_type_usinage, page_materiaux, page_vis, page_resultat_taraudage]
alesage = [page_type_usinage, page_materiaux, page_resultat_alesage]

# Fenetre principale
main_fenetre = tk.Tk()
main_fenetre.title("Calcul des conditions de coupe")

# Calcul de la position (centre)
largeur_fenetre, hauteur_fenetre = 500, 300
largeur_ecran, hauteur_ecran = main_fenetre.winfo_screenwidth(), main_fenetre.winfo_screenheight()
position_x, position_y = (largeur_ecran // 2) - (largeur_fenetre // 2), (hauteur_ecran // 2) - (hauteur_fenetre // 2)
main_fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_x}+{position_y}")

# Afficher la première page
changement_page(main_fenetre, fraisage, 0)

# Lancer la boucle principale
main_fenetre.mainloop()