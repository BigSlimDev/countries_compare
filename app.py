import tkinter as tk

from country_actions import CountryAppController

window = tk.Tk()
window.title("Country Relocation & Culture Guide")
window.geometry("850x750")
window.configure(bg="#F4F6F8")

# Title label
title_label = tk.Label(
    window,
    text="🌍 Country Relocation & Culture Guide",
    font=("Segoe UI", 22, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
title_label.pack(pady=20)

# This handles the Search section of our GUI
search_frame = tk.LabelFrame(
    window,
    text="Search Information",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=15,
    bg="#F4F6F8",
    fg="#34495E"
)
search_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    search_frame,
    text="Country:",
    font=("Segoe UI", 11),
    bg="#F4F6F8"
).grid(row=0, column=0, sticky="w", pady=8)

country_entry = tk.Entry(search_frame, width=40, font=("Segoe UI", 11))
country_entry.grid(row=0, column=1, padx=10)

tk.Label(
    search_frame,
    text="Purpose (study, travel, relocation):",
    font=("Segoe UI", 11),
    bg="#F4F6F8"
).grid(row=1, column=0, sticky="w", pady=8)

purpose_entry = tk.Entry(search_frame, width=40, font=("Segoe UI", 11))
purpose_entry.grid(row=1, column=1, padx=10)

# Buttons row
button_frame = tk.Frame(search_frame, bg="#F4F6F8")
button_frame.grid(row=2, column=0, columnspan=2, pady=15)
# This handles the search button of the GUI
search_button = tk.Button(
    button_frame,
    text="🔍 Search",
    bg="#3498DB",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12
)
search_button.pack(side="left", padx=10)
# This handles the Generate section of our GUI
generate_button = tk.Button(
    button_frame,
    text="📄 Generate Guide",
    bg="#27AE60",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15
)
generate_button.pack(side="left", padx=10)

# This handles the Checklist section of our GUI
check_list_button = tk.Button(
    button_frame,
    text="📋 Checklist",
    bg="#2C3E50",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=12
)
check_list_button.pack(side="left", padx=10)

# This handles the Save section of our GUI

save_button = tk.Button(
    button_frame,
    text="💾 Save Country",
    bg="#9B59B6",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15
)
save_button.pack(side="left", padx=10)

save_button_guide = tk.Button(
    button_frame,
    text="💾 Save Guide",
    bg="#2C3E50",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15
)
save_button_guide.pack(side="left", padx=10)

# This handles the View saved  favorite sections of our GUI
view_saved_button = tk.Button(
    button_frame,
    text="🔍 View Saved Countries",
    bg="#AD2464",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=20
)
view_saved_button.pack(side="left", padx=10)

# This handles the View saved guide sections of our GUI
view_saved_bu= tk.Button(
    button_frame,
    text="🔍 View Saved Guide",
    bg="#307C56",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=17
)
view_saved_bu.pack(side="left", padx=10)





# This is for the compare section of our gui
compare_frame = tk.LabelFrame(
    window,
    text="Compare Countries",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=15,
    bg="#F4F6F8",
    fg="#34495E"
)
compare_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    compare_frame,
    text="Country 1:",
    font=("Segoe UI", 11),
    bg="#F4F6F8"
).grid(row=0, column=0, pady=8)

country1_entry = tk.Entry(compare_frame, width=30, font=("Segoe UI", 11))
country1_entry.grid(row=0, column=1, padx=10)

tk.Label(
    compare_frame,
    text="Country 2:",
    font=("Segoe UI", 11),
    bg="#F4F6F8"
).grid(row=0, column=2, pady=8)

country2_entry = tk.Entry(compare_frame, width=30, font=("Segoe UI", 11))
country2_entry.grid(row=0, column=3, padx=10)

compare_button = tk.Button(
    compare_frame,
    text="⚖ Compare",
    bg="#E67E22",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15
)
compare_button.grid(row=1, column=0, columnspan=4, pady=15)

# The output section of our GUI
output_frame = tk.LabelFrame(
    window,
    text="Results",
    font=("Segoe UI", 12, "bold"),
    padx=15,
    pady=15,
    bg="#F4F6F8",
    fg="#34495E"
)
output_frame.pack(fill="both", expand=True, padx=20, pady=15)

# Frame to hold text widget and scrollbar
text_frame = tk.Frame(output_frame)
text_frame.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

# Text widget
output = tk.Text(
    text_frame,
    height=18,
    width=90,
    font=("Consolas", 10),
    bg="white",
    fg="#2C3E50",
    relief="solid",
    bd=1,
    yscrollcommand=scrollbar.set
)
output.pack(side="left", fill="both", expand=True)

# Connect scrollbar to text widget
scrollbar.config(command=output.yview)

controller = CountryAppController(
    country_entry=country_entry,
    purpose_entry=purpose_entry,
    country1_entry=country1_entry,
    country2_entry=country2_entry,
    output=output,
)

search_button.config(command=controller.search_country)
save_button.config(command=controller.save_favorite_country)
save_button_guide.config(command=controller.save_guide)
compare_button.config(command=controller.compare_countries)
generate_button.config(command=controller.generate_guide)
check_list_button.config(command=controller.check_list)
view_saved_button.config(command=controller.view_saved)
view_saved_bu.config(command=controller.view_saved_guide)


window.mainloop()




