import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import datetime
import pycountry
import pycountry_convert as pc

current_year = datetime.now().year

# Build full country list
countries = sorted([country.name for country in pycountry.countries])

def get_continent(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        country_code = country.alpha_2
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continents = {
            "NA": "North America",
            "SA": "South America",
            "EU": "Europe",
            "AF": "Africa",
            "AS": "Asia",
            "OC": "Oceania"
        }
        return continents.get(continent_code, "Unknown")
    except:
        return "Unknown"

def classify_generation(age):
    birth_year = current_year - age
    if 1940 <= birth_year <= 1959:
        return "Boomer", "primary", birth_year
    elif 1960 <= birth_year <= 1979:
        return "Gen X", "success", birth_year
    elif 1980 <= birth_year <= 1999:
        return "Millennial", "warning", birth_year
    elif 2000 <= birth_year <= 2009:
        return "Gen Z", "info", birth_year
    elif 2010 <= birth_year <= 2019:
        return "Gen Alpha", "danger", birth_year
    elif 2020 <= birth_year <= 2029:
        return "Gen Beta", "secondary", birth_year
    else:
        return "Outside Model", "dark", birth_year

def classify():
    country = country_box.get()

    try:
        age = int(age_entry.get())
    except:
        result_label.config(text="Enter a valid age")
        return

    continent = get_continent(country)
    generation, color, birth_year = classify_generation(age)

    result_label.config(
        text=(
            f"Country: {country}\n"
            f"Continent: {continent}\n"
            f"Birth Year: {birth_year}\n"
            f"Generation: {generation}"
        ),
        bootstyle=color
    )

# Create window
app = tb.Window(themename="flatly")
app.title("Global Generation Classifier")
app.geometry("420x360")

tb.Label(app, text="Select Country", font=("Arial", 12)).pack(pady=8)

country_box = tb.Combobox(app, values=countries)
country_box.pack(pady=5)
country_box.focus()

tb.Label(app, text="Enter Age", font=("Arial", 12)).pack(pady=8)

age_entry = tb.Entry(app)
age_entry.pack()

tb.Button(app, text="Classify", command=classify, bootstyle=PRIMARY).pack(pady=15)

result_label = tb.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

app.mainloop()