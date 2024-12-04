import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import pi

def get_vitesse_de_coupe(materiau, outil, operation):
    vitesse_de_coupe = {
        # Ebauche - ARS
        ("Acier non allié (P)", "ARS", "Ebauche"): 50,
        ("Acier faiblement allié (P)", "ARS", "Ebauche"): 40,
        ("Acier fortement allié (P)", "ARS", "Ebauche"): 30,
        ("Acier moulé fortement allié (P)", "ARS", "Ebauche"): 30,
        ("Inox (M)", "ARS", "Ebauche"): 25,
        ("Fonte lamellaire (K)", "ARS", "Ebauche"): 40,
        ("Fonte modulaire (K)", "ARS", "Ebauche"): 50,
        ("Fonte sphéroïdale (K)", "ARS", "Ebauche"): 55,
        ("Aluminium faible dureté + silicium comme 2030 (N)", "ARS", "Ebauche"): 250,
        ("Aluminium forte dureté + silicium comme 6060(N)", "ARS", "Ebauche"): 120,
        ("Aluminium +12% de silicium (N)", "ARS", "Ebauche"): 80,

        # Finition - ARS
        ("Acier non allié (P)", "ARS", "Finition"): 40,
        ("Acier faiblement allié (P)", "ARS", "Finition"): 30,
        ("Acier fortement allié (P)", "ARS", "Finition"): 15,
        ("Acier moulé fortement allié (P)", "ARS", "Finition"): 20,
        ("Inox (M)", "ARS", "Finition"): 20,
        ("Fonte lamellaire (K)", "ARS", "Finition"): 20,
        ("Fonte modulaire (K)", "ARS", "Finition"): 30,
        ("Fonte sphéroïdale (K)", "ARS", "Finition"): 35,
        ("Aluminium faible dureté + silicium comme 2030 (N)", "ARS", "Finition"): 200,
        ("Aluminium forte dureté + silicium comme 6060(N)", "ARS", "Finition"): 100,
        ("Aluminium +12% de silicium (N)", "ARS", "Finition"): 70,

        # Ebauche - Carbure
        ("Acier non allié (P)", "Carbure", "Ebauche"): 40,
        ("Acier faiblement allié (P)", "Carbure", "Ebauche"): 20,
        ("Acier fortement allié (P)", "Carbure", "Ebauche"): 15,
        ("Acier moulé faiblement allié (P)", "Carbure", "Ebauche"): 20,
        ("Inox (M)", "Carbure", "Ebauche"): 20,
        ("Fonte lamellaire (K)", "Carbure", "Ebauche"): 20,
        ("Fonte modulaire (K)", "Carbure", "Ebauche"): 30,
        ("Fonte sphéroïdale (K)", "Carbure", "Ebauche"): 35,
        ("Aluminium faible dureté + silicium comme 2030 (N)", "Carbure", "Ebauche"): 200,
        ("Aluminium forte dureté + silicium comme 6060(N)", "Carbure", "Ebauche"): 100,
        ("Aluminium +12% de silicium (N)", "Carbure", "Ebauche"): 70,

        # Finition - Carbure
        ("Acier non allié (P)", "Carbure", "Finition"): 120,
        ("Acier faiblement allié (P)", "Carbure", "Finition"): 80,
        ("Acier fortement allié (P)", "Carbure", "Finition"): 75,
        ("Acier moulé fortement allié (P)", "Carbure", "Finition"): 80,
        ("Inox (M)", "Carbure", "Finition"): 60,
        ("Fonte lamellaire (K)", "Carbure", "Finition"): 20,
        ("Fonte modulaire (K)", "Carbure", "Finition"): 30,
        ("Fonte sphéroïdale (K)", "Carbure", "Finition"): 35,
        ("Aluminium faible dureté + silicium comme 2030 (N)", "Carbure", "Finition"): 150,
        ("Aluminium forte dureté + silicium comme 6060(N)", "Carbure", "Finition"): 90,
        ("Aluminium +12% de silicium (N)", "Carbure", "Finition"): 60,
    }

    # Retourner la vitesse de coupe pour la combinaison sélectionnée
    return vitesse_de_coupe.get((materiau, outil, operation), None)

def page_type_usinage(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un type d'usinage", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des types d'usinage
    types_usinage = ["Fraisage", "Tournage", "Percage", "Traudage", "Alésage"]
    combobox_usinage = ttk.Combobox(fenetre, values=types_usinage)
    combobox_usinage.set(types_usinage[0])
    combobox_usinage.pack(pady=10)

    # Bouton suivant pour passer à la page suivante
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changer_page(index_page + 1))
    bouton_suivant.pack(pady=20)

def page_materiaux(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

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

    # Bouton suivant pour passer à la page suivante
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changer_page(index_page + 1))
    bouton_suivant.pack(pady=20)

def page_outil(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner un outil", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des outils
    outils = ["ARS", "Carbure"]
    combobox_outils = ttk.Combobox(fenetre, values=outils)
    combobox_outils.set(outils[0])
    combobox_outils.pack(pady=10)

    # Bouton suivant pour passer à la page suivante
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changer_page(index_page + 1))
    bouton_suivant.pack(pady=20)

def page_operation(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Titre de la page
    titre = tk.Label(fenetre, text="Sélectionner une opération", font=("Arial", 16))
    titre.pack(pady=20)

    # Liste des opérations
    operations = ["Ebauche", "Finition", "Tronconnage", "Gorge", "Filetage"]
    combobox_operation = ttk.Combobox(fenetre, values=operations)
    combobox_operation.set(operations[0])
    combobox_operation.pack(pady=10)

    # Bouton suivant pour passer à la page suivante
    bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: changer_page(index_page + 1))
    bouton_suivant.pack(pady=20)

def page_rayon_bec(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Titre de la page
    titre_rayon_bec = tk.Label(fenetre, text="Sélectionner un rayon de plaquette", font=("Arial", 16))
    titre_rayon_bec.pack(pady=20)

    # Frame pour les champs d'entrée
    rayon_bec_frame = tk.Frame(fenetre)
    rayon_bec_frame.pack(pady=20)

    label_rayon_bec = tk.Label(rayon_bec_frame, text="Entrez un rayon positif :")
    label_rayon_bec.pack(pady=5)

    entry_rayon_bec = tk.Entry(rayon_bec_frame)
    entry_rayon_bec.pack(pady=10)

    def on_button_click():
        try:
            rayon = float(entry_rayon_bec.get())
            if rayon > 0:
                changer_page(index_page + 1)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un rayon positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    button_suivant_rayon_bec = tk.Button(rayon_bec_frame, text="Suivant", command=on_button_click)
    button_suivant_rayon_bec.pack(pady=20)

def page_diametre_piece(fenetre, changer_page, index_page):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Titre de la page
    titre_diametre_piece = tk.Label(fenetre, text="Sélectionner le diamètre de la pièce", font=("Arial", 16))
    titre_diametre_piece.pack(pady=20)

    # Frame pour les champs d'entrée
    diametre_piece_frame = tk.Frame(fenetre)
    diametre_piece_frame.pack(pady=20)

    label_diametre_piece = tk.Label(diametre_piece_frame, text="Entrez un diamètre positif :")
    label_diametre_piece.pack(pady=5)

    entry_diametre_piece = tk.Entry(diametre_piece_frame)
    entry_diametre_piece.pack(pady=10)

    def on_button_click():
        try:
            diametre = float(entry_diametre_piece.get())
            if diametre > 0:
                changer_page(index_page + 1)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un diamètre positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    button_suivant_diametre_piece = tk.Button(diametre_piece_frame, text="Suivant", command=on_button_click)
    button_suivant_diametre_piece.pack(pady=20)

def page_resultat_tournage(fenetre, rayon_bec, rayon, diametre, operation, outil, materiaux, avance, profondeur_passe, rotation):
    # Effacer la fenêtre
    for widget in fenetre.winfo_children():
        widget.pack_forget()

    # Afficher les résultats
    titre_resultat = tk.Label(fenetre, text="Résultats", font=("Arial", 16))
    titre_resultat.pack(pady=20)

    resultat_text = f"Rayon: {rayon} mm\nDiamètre: {diametre} mm\nOpération: {operation}\nOutil: {outil}\nMatériau: {materiaux}\nAvance: {avance} mm/min\nProfondeur de passe: {profondeur_passe} mm\nRotation: {rotation} tr/min"
    label_resultat = tk.Label(fenetre, text=resultat_text, font=("Arial", 12))
    label_resultat.pack(pady=20)

    # Bouton Terminer
    bouton_terminer = tk.Button(fenetre, text="Terminer", command=fenetre.quit)
    bouton_terminer.pack(pady=20)

pages = [page_type_usinage, page_materiaux, page_rayon_bec, page_diametre_piece, page_resultat_tournage]
index_page = 0

# Fonction de changement de page
def changer_page(index):
    if index < len(pages):
        pages[index](main_fenetre, changer_page, index)


# Fenetre principale
main_fenetre = tk.Tk()
main_fenetre.title("Calcul des conditions de coupe")

# Calcul de la position (centre)
largeur_fenetre, hauteur_fenetre = 500, 300
largeur_ecran, hauteur_ecran = main_fenetre.winfo_screenwidth(), main_fenetre.winfo_screenheight()
position_x, position_y = (largeur_ecran // 2) - (largeur_fenetre // 2), (hauteur_ecran // 2) - (hauteur_fenetre // 2)
main_fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_x}+{position_y}")

# Afficher la première page
changer_page(0)

# Lancer la boucle principale
main_fenetre.mainloop()