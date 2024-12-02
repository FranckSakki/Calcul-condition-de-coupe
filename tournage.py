import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

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
        ("Titane (S)", "ARS", "Ebauche"): 0,
        ("Plastique", "ARS", "Ebauche"): 0,
        ("Bois", "ARS", "Ebauche"): 0,

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
        ("Titane (S)", "ARS", "Finition"): 5,
        ("Plastique", "ARS", "Finition"): 0,
        ("Bois", "ARS", "Finition"): 0,

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
        ("Titane (S)", "Carbure", "Ebauche"): 0,
        ("Plastique", "Carbure", "Ebauche"): 0,
        ("Bois", "Carbure", "Ebauche"): 0,

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
        ("Titane (S)", "Carbure", "Finition"): 0,
        ("Plastique", "Carbure", "Finition"): 0,
        ("Bois", "Carbure", "Finition"): 0
    }

    # Retourner la vitesse de coupe pour la combinaison sélectionnée
    return vitesse_de_coupe.get((materiau, outil, operation), None)

def afficher_materiaux(fenetre, type_usinage_frame, type_usinage):
    type_usinage_frame.pack_forget()

    materiaux_frame = tk.Frame(fenetre)
    materiaux_frame.pack(pady=20)

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
                 "Aluminium +12% de silicium (N)",
                 "Titane (S)",
                 "Plastique",
                 "Bois"]
    combobox_materiaux = ttk.Combobox(materiaux_frame, values=materiaux, width=45)
    combobox_materiaux.set(materiaux[0])
    combobox_materiaux.pack(pady=10)

    button_suivant_outil = tk.Button(materiaux_frame, text="Suivant", command=lambda: afficher_outil(fenetre, materiaux_frame, combobox_materiaux, type_usinage))
    button_suivant_outil.pack()

def afficher_outil(fenetre, materiaux_frame, combobox_materiaux, type_usinage):
    materiaux_frame.pack_forget()

    outil_frame = tk.Frame(fenetre)
    outil_frame.pack(pady=20)

    outils = ["ARS", "Carbure"]
    combobox_outil = ttk.Combobox(outil_frame, values=outils)
    combobox_outil.set(outils[0])
    combobox_outil.pack(pady=10)

    button_suivant_outil = tk.Button(outil_frame, text="Suivant", command=lambda: afficher_operation(fenetre, outil_frame, combobox_outil, combobox_materiaux, type_usinage))
    button_suivant_outil.pack()

def afficher_operation(fenetre, outil_frame, combobox_outil, combobox_materiaux, type_usinage):
    outil_frame.pack_forget()

    operation_frame = tk.Frame(fenetre)
    operation_frame.pack(pady=20)

    operation = ["Ebauche", "Finition", "Tronconnage", "Gorge", "Filetage"]
    combobox_operation = ttk.Combobox(operation_frame, values=operation)
    combobox_operation.set(operation[0])
    combobox_operation.pack(pady=10)

    button_suivant_operation = tk.Button(operation_frame, text="Suivant", command=lambda: afficher_rayon_bec(fenetre, operation_frame, combobox_operation, combobox_outil, combobox_materiaux, type_usinage))
    button_suivant_operation.pack()

def afficher_rayon_bec(fenetre, operation_frame, combobox_operation, combobox_outil, combobox_materiaux, type_usinage):
    operation_selected = combobox_operation.get()
    outil_selected = combobox_outil.get()
    materiaux_selected = combobox_materiaux.get()

    operation_frame.destroy()

    rayon_bec_frame = tk.Frame(fenetre)
    rayon_bec_frame.pack(pady=20)

    label_rayon_bec = tk.Label(rayon_bec_frame, text="Entrez un rayon positif :")
    label_rayon_bec.pack(pady=5)

    entry_rayon_bec = tk.Entry(rayon_bec_frame)
    entry_rayon_bec.pack(pady=10)

    label_diametre = tk.Label(rayon_bec_frame, text="Entrez le diamètre de la pièce (en mm) :")
    label_diametre.pack(pady=5)

    entry_diametre = tk.Entry(rayon_bec_frame)
    entry_diametre.pack(pady=10)

    def on_button_click():
        try:
            rayon = float(entry_rayon_bec.get())
            diametre = float(entry_diametre.get())

            if rayon > 0 and diametre > 0:
                # Calcul de l'avance et de la profondeur de passe
                if operation_selected == "Ebauche":
                    avance = 0.4 * rayon
                    profondeur_passe = 4 * rayon
                elif operation_selected == "Finition":
                    avance = 0.2 * rayon
                    profondeur_passe = 0.7 * rayon
                else:
                    avance = 0.1
                    profondeur_passe = 0.5

                vitesse_coupe = get_vitesse_de_coupe(materiaux_selected, outil_selected, operation_selected)
                if vitesse_coupe:
                    rotation = round((1000 * vitesse_coupe) / (math.pi * diametre))
                    avance = round(avance, 3)
                    profondeur_passe = round(avance, 3)
                    afficher_resultat(fenetre, rayon_bec_frame, rayon, diametre, operation_selected, outil_selected, materiaux_selected, type_usinage, avance, profondeur_passe, rotation)
                else:
                    messagebox.showerror("Erreur", "Combinée matériau-outil-opération non implémenté.")
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un rayon et un diamètre valides.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    button_suivant_rayon_bec = tk.Button(rayon_bec_frame, text="Suivant", command=on_button_click)
    button_suivant_rayon_bec.pack()

def afficher_resultat(fenetre, rayon_bec_frame, rayon, diametre, operation_selected, outil_selected, materiaux_selected, type_usinage, avance, profondeur_passe, rotation):
    rayon_bec_frame.destroy()  # Détruire le frame précédent

    resultat_frame = tk.Frame(fenetre)
    resultat_frame.pack(pady=20)

    # Colonnes
    label_resume = tk.Label(resultat_frame, text="Résumé des sélections")
    label_resume.grid(row=0, column=0, padx=10, pady=5)
    label_resultat = tk.Label(resultat_frame, text="Résultats des calculs")
    label_resultat.grid(row=0, column=1, padx=10, pady=5)

    # Colonne 1 (Résumé des sélections)
    label_type_usinage = tk.Label(resultat_frame, text=f"Type d'usinage : {type_usinage}")
    label_type_usinage.grid(row=1, column=0, padx=10, pady=5)
    label_materiaux = tk.Label(resultat_frame, text=f"Matériaux : {materiaux_selected}")
    label_materiaux.grid(row=2, column=0, padx=10, pady=5)
    label_outil = tk.Label(resultat_frame, text=f"Outil : {outil_selected}")
    label_outil.grid(row=3, column=0, padx=10, pady=5)
    label_selections = tk.Label(resultat_frame, text=f"Opération : {operation_selected}")
    label_selections.grid(row=4, column=0, padx=10, pady=5)
    label_rayon_bec = tk.Label(resultat_frame, text=f"Rayon de bec : {rayon}")
    label_rayon_bec.grid(row=5, column=0, padx=10, pady=5)

    # Colonne 2 (Résultats des calculs)
    label_calcul_1 = tk.Label(resultat_frame, text=f"Avance en mm/tr : {avance}")
    label_calcul_1.grid(row=1, column=1, padx=10, pady=5)
    label_calcul_2 = tk.Label(resultat_frame, text=f"Profondeur de passe en mm : {profondeur_passe}")
    label_calcul_2.grid(row=2, column=1, padx=10, pady=5)
    label_calcul_3 = tk.Label(resultat_frame, text=f"Rotation en tr/min : {rotation}")
    label_calcul_3.grid(row=3, column=1, padx=10, pady=5)

    button_suivant = tk.Button(resultat_frame, text="Suivant", command=lambda: print("Prochaine étape"))
    button_suivant.grid(row=6, column=1, pady=20)

