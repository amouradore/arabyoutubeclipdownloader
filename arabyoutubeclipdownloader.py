# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import yt_dlp

def download_youtube_clip(url, start_time, end_time, output_filename):
    """
    Télécharge un extrait de vidéo YouTube à partir de start_time et end_time (en secondes)
    et sauvegarde le résultat dans output_filename.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Meilleure qualité
        'outtmpl': output_filename,
        'download_ranges': lambda info, ctx: [{
            'start_time': start_time,
            'end_time': end_time,
        }],
        'force_generic_extractor': True,
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def on_submit():
    """
    Récupère les valeurs entrées par l'utilisateur, convertit les minutes en secondes,
    puis lance le téléchargement de l'extrait vidéo.
    """
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("خطأ", "الرجاء إدخال رابط الفيديو")
        return

    try:
        start_time_min = float(start_time_entry.get().strip())
        end_time_min = float(end_time_entry.get().strip())
    except ValueError:
        messagebox.showerror("خطأ", "الرجاء إدخال وقت صحيح (بالدقائق)")
        return

    # Conversion des minutes en secondes
    start_time = int(start_time_min * 60)
    end_time = int(end_time_min * 60)

    output_filename = output_filename_entry.get().strip()
    if not output_filename:
        messagebox.showerror("خطأ", "الرجاء إدخال اسم ملف الإخراج")
        return

    if not output_filename.endswith('.mp4'):
        output_filename += '.mp4'

    try:
        download_youtube_clip(url, start_time, end_time, output_filename)
        messagebox.showinfo("نجاح", f"تم التحميل بنجاح!\nتم حفظ الملف: {output_filename}")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ: {str(e)}")

def browse_output_location():
    """
    Ouvre une boîte de dialogue pour choisir l'emplacement du fichier de sortie.
    """
    filename = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("????? MP4", "*.mp4")])
    if filename:
        output_filename_entry.delete(0, tk.END)
        output_filename_entry.insert(0, filename)

# Création de la fenêtre principale
root = tk.Tk()
root.title("تحميل مقاطع يوتيوب")
root.geometry("600x250")

# Configuration de la police pour supporter l'arabe
arabic_font = ('Arial', 10)  # ou tout autre police qui supporte l'arabe

# Utilisation d'un thème ttk pour une interface plus moderne
style = ttk.Style(root)
style.theme_use("clam")  # Vous pouvez essayer d'autres thèmes comme "alt", "default", etc.

# Ajouter ceci après la création de root
style = ttk.Style()
style.configure('Arabic.TButton', font=arabic_font)

# Création d'un cadre pour organiser les widgets avec un padding
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill='both')

# Champ de saisie pour l'URL
url_label = ttk.Label(frame, text="رابط الفيديو:", font=arabic_font)
url_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
url_entry = ttk.Entry(frame, width=50, justify='right')
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Champ de saisie pour le temps de début (en minutes)
start_time_label = ttk.Label(frame, text="وقت البداية (بالدقائق):", font=arabic_font)
start_time_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
start_time_entry = ttk.Entry(frame, width=20, justify='right')
start_time_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Champ de saisie pour le temps de fin (en minutes)
end_time_label = ttk.Label(frame, text="وقت النهاية (بالدقائق):", font=arabic_font)
end_time_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
end_time_entry = ttk.Entry(frame, width=20, justify='right')
end_time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Champ de saisie pour le nom du fichier de sortie
output_filename_label = ttk.Label(frame, text="اسم ملف الإخراج:", font=arabic_font)
output_filename_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
output_filename_entry = ttk.Entry(frame, width=50, justify='right')
output_filename_entry.grid(row=3, column=1, padx=5, pady=5)
browse_button = ttk.Button(frame, text="تصفح", command=browse_output_location, style='Arabic.TButton')
browse_button.grid(row=3, column=2, padx=5, pady=5)

# Bouton pour lancer le téléchargement
submit_button = ttk.Button(frame, text="تحميل", command=on_submit, style='Arabic.TButton')
submit_button.grid(row=4, column=0, columnspan=3, pady=15)

# Démarrage de la boucle principale
root.mainloop()

print("????? ????????")