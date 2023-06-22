import customtkinter
from customtkinter import filedialog
from PIL import Image
from pipeline import*


#Functions
def generate_art():
    #Art Characteristics 
    medium = medium_entry.get() #illustration, oil painting, 3D Rendering, photography, digital painting, 
    style = style_entry.get() #artistic style
    artist = artist_entry.get() #specific artists will give art in the style of their work
    lighting = lighting_entry.get() #changes the lighting of the art
    image_color = image_color_entry.get() #adds a color theme to the art
    additional_details = add_details_entry.get() #Any other detials not mentioned

    #Physical Character Characteristics
    gender = gender_entry.get()
    race = race_entry.get()
    skin = skin_entry.get()
    build = build_entry.get()
    height = height_entry.get()
    c_class = c_class_entry.get()
    hair = hair_entry.get()
    eyes = eyes_entry.get()
    head = head_entry.get()
    face = face_entry.get()
    nose = nose_entry.get()
    mouth = mouth_entry.get()
    ears = eyes_entry.get()
    pose = pose_entry.get()

    #Character Equipment
    weapon = weapon_entry.get()
    chestarmor = chestarmor_entry.get()
    leggings = leggings_entry.get()
    gloves = gloves_entry.get()
    boots = boots_entry.get()
    helmet = helmet_entry.get()
    belt = belt_entry.get()
    jewlery = jewelry_entry.get()
    
    user_prompt = f'(highly detailed, 8k portrait, finely detailed eyes, masterpiece: 1.5), {style}, {lighting}, {image_color} {medium}, {gender}, {race}, {skin}, {build}, {height}, {c_class}, {hair}, {eyes}, {head}, {face}, {nose}, {mouth}, {ears}, {pose}, {weapon}, {chestarmor}, {leggings}, {gloves}, {boots}, {helmet}, {belt}, {jewlery}, {additional_details}'
    negative_prompt = "text, watermark, logo, back to viewer, extra fingers, missing fingers, blurry, deformed face, distorted face, distorted eyes, mutated, disfigured, poorly drawn face, bad anatomy, close up, (uneven pupils, unsymmetrical face, unsymmetrical eyes: 1.5), nsfw, revealing clothing, lowres, low resolution, poor resolution"
    image = pipe(user_prompt, negative_prompt=negative_prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images[0]

    #Saves the image
    image.save("image.png")

    display_image()

#Diplays the image on customTkinter GUI
def display_image():
    display = customtkinter.CTkImage(dark_image=Image.open("image.png"), size=(520, 520))
    image_label = customtkinter.CTkLabel(image_frame, width=512, height= 512, image=display, text="")
    image_label.grid(row=0, column=0, padx=25, pady=10, sticky="nw")

#Saves the image and asks for the filename
def save_image():
    image_to_save = Image.open("image.png")
    save_path = filedialog.asksaveasfilename(title="Save Image as", defaultextension=".jpg")
    image_to_save.save(save_path)

#Switches between the two models through the GUI
def switch_model():
    global modelname
    global pipe
    if modelname == "Lykon/NeverEnding-Dream":
        modelname = "Ojimi/anime-kawai-diffusion"
        pipe = StableDiffusionPipeline.from_pretrained(modelname, torch_dtype=torch.float16, safety_checker = None)
        pipe = pipe.to("cuda")
        image_frame_label.configure(text='Model Name: Ojimi/anime-kawai-diffusion')
        image_frame_label.grid(row=7, column=0)
    elif modelname == "Ojimi/anime-kawai-diffusion":
        modelname = "Lykon/NeverEnding-Dream"
        pipe = StableDiffusionPipeline.from_pretrained(modelname, torch_dtype=torch.float16, safety_checker = None)
        pipe = pipe.to("cuda")
        image_frame_label.configure(text='Model Name: Lykon/NeverEnding-Dream')
        image_frame_label.grid(row=7, column=0)


        

#CustomTKinter UI

#UI Appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Root window
root = customtkinter.CTk()
root.geometry("650x650")
root.maxsize(650, 650)
scrollable_frame = customtkinter.CTkScrollableFrame(root)
scrollable_frame.grid_columnconfigure(0, weight=1)
scrollable_frame.pack(fill="both", expand="true")
label = customtkinter.CTkLabel(master=scrollable_frame, text= "AI Character Creator")

#Fonts
header_font = customtkinter.CTkFont(family='Roboto', size=20)

#Frames
art_char_frame_label = customtkinter.CTkLabel(master=scrollable_frame, text="Art Characteristics:", font=header_font)
art_char_frame_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
art_char_frame = customtkinter.CTkFrame(master=scrollable_frame)
art_char_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")

physical_char_frame_label = customtkinter.CTkLabel(master=scrollable_frame, text="Character's Physical traits:", font=header_font)
physical_char_frame_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
physical_char_frame = customtkinter.CTkFrame(master=scrollable_frame)
physical_char_frame.grid(row=3, column=0, padx=20, pady=10, sticky="w")

equipment_frame_label = customtkinter.CTkLabel(master=scrollable_frame, text="Character equipment:", font=header_font)
equipment_frame_label.grid(row=4, column=0, pady=10, padx=10, sticky="w")
equipment_frame = customtkinter.CTkFrame(master=scrollable_frame)
equipment_frame.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")

button_frame = customtkinter.CTkFrame(master=scrollable_frame)
button_frame.grid(row=6, column=0, padx=20, pady=10)

image_frame = customtkinter.CTkFrame(master=scrollable_frame)
image_frame.grid(row=8, column=0, padx=20, pady=10)
image_frame_label =customtkinter.CTkLabel(master=scrollable_frame, text=f'Model Name: {modelname}')
image_frame_label.grid(row=7, column=0)

#Art Characteristics Labels and Entries

style_label = customtkinter.CTkLabel(master=art_char_frame, text="Style")
style_label.grid(pady=12, padx=18, row=1, column=0)
style_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text="realistic, anime....")
style_entry.grid(pady=12, padx=18, row=1, column=1)

medium_label = customtkinter.CTkLabel(master=art_char_frame, text="Medium")
medium_label.grid(pady=12, padx=18, row=2, column=0)
medium_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text="painting, digital art...")
medium_entry.grid(pady=12, padx=18, row=2, column=1)

lighting_label = customtkinter.CTkLabel(master=art_char_frame, text="Lighting")
lighting_label.grid(pady=12, padx=18, row=3, column=0)
lighting_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text="bright, sidelighting....")
lighting_entry.grid(pady=12, padx=18, row=3, column=1)

image_color_label = customtkinter.CTkLabel(master=art_char_frame, text="Image Color")
image_color_label.grid(pady=12, padx=18, row=1, column=2)
image_color_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text="Golden, purple...")
image_color_entry.grid(pady=12, padx=18, row=1, column=3)

artist_label = customtkinter.CTkLabel(master=art_char_frame, text="Artist")
artist_label.grid(pady=12, padx=18, row=2, column=2)
artist_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text="Picasso, da Vinci...")
artist_entry.grid(pady=12, padx=18, row=2, column=3)

add_details_label = customtkinter.CTkLabel(master=art_char_frame, text="Additional Details")
add_details_label.grid(pady=12, padx=18, row=3, column=2)
add_details_entry = customtkinter.CTkEntry(master=art_char_frame, placeholder_text=".....")
add_details_entry.grid(pady=12, padx=18, row=3, column=3)


#Character Physical Characteristics labels and entries

gender_label = customtkinter.CTkLabel(master=physical_char_frame, text="Gender")
gender_label.grid(pady=12, padx=20, row=1, column=0)
gender_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="male, female...")
gender_entry.grid(pady=12, padx=20, row=1, column=1)

race_label = customtkinter.CTkLabel(master=physical_char_frame, text="Race")
race_label.grid(pady=12, padx=20, row=2, column=0)
race_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="human, elf, orc...")
race_entry.grid(pady=12, padx=20, row=2, column=1)

skin_label = customtkinter.CTkLabel(master=physical_char_frame, text="Skin")
skin_label.grid(pady=12, padx=20, row=3, column=0)
skin_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="white, black...")
skin_entry.grid(pady=12, padx=20, row=3, column=1)

build_label = customtkinter.CTkLabel(physical_char_frame, text="Build")
build_label.grid(pady=12, padx=20, row=1, column=2)
build_entry = customtkinter.CTkEntry(physical_char_frame, placeholder_text="muscular, slim...")
build_entry.grid(pady=12, padx=20, row=1, column=3)

height_label = customtkinter.CTkLabel(master=physical_char_frame, text="Height")
height_label.grid(pady=12, padx=20, row=2, column=2)
height_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="tall, short...")
height_entry.grid(pady=12, padx=20, row=2, column=3)

c_class_label = customtkinter.CTkLabel(master=physical_char_frame, text="Character Class")
c_class_label.grid(pady=12, padx=20, row=3, column=2)
c_class_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="mage, warrior...")
c_class_entry.grid(pady=12, padx=20, row=3, column=3)

hair_label = customtkinter.CTkLabel(master=physical_char_frame, text="Hair")
hair_label.grid(pady=12, padx=20, row=4, column=0)
hair_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(length, style, color)hair...")
hair_entry.grid(pady=12, padx=20, row=4, column=1)

eyes_label = customtkinter.CTkLabel(master=physical_char_frame, text="Eyes")
eyes_label.grid(pady=12, padx=20, row=5, column=0)
eyes_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(color, shape)eyes...")
eyes_entry.grid(pady=12, padx=20, row=5, column=1)

head_label = customtkinter.CTkLabel(master=physical_char_frame, text="Head")
head_label.grid(pady=12, padx=20, row=6, column=0)
head_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(small, round)head")
head_entry.grid(pady=12, padx=20, row=6, column=1)

face_label = customtkinter.CTkLabel(master=physical_char_frame, text="Face")
face_label.grid(pady=12, padx=20, row=4, column=2)
face_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(pretty, rough)face")
face_entry.grid(pady=12, padx=20, row=4, column=3)

nose_label = customtkinter.CTkLabel(master=physical_char_frame, text="Nose")
nose_label.grid(pady=12, padx=20, row=5, column=2)
nose_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(long, thick)nose")
nose_entry.grid(pady=12, padx=20, row=5, column=3)

mouth_label = customtkinter.CTkLabel(master=physical_char_frame, text="Mouth")
mouth_label.grid(pady=12, padx=20, row=6, column=2)
mouth_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(large, puffy)mouth")
mouth_entry.grid(pady=12, padx=20, row=6, column=3)

ears_label = customtkinter.CTkLabel(master=physical_char_frame, text="Ears")
ears_label.grid(pady=12, padx=20, row=7, column=0)
ears_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="(pointy, long)ears")
ears_entry.grid(pady=12, padx=20, row=7, column=1)

pose_label = customtkinter.CTkLabel(master=physical_char_frame, text="Pose")
pose_label.grid(pady=12, padx=20, row=7, column=2)
pose_entry = customtkinter.CTkEntry(master=physical_char_frame, placeholder_text="sitting, standing...")
pose_entry.grid(pady=12, padx=20, row=7, column=3)

#Character Equipment labels and entries

weapon_label = customtkinter.CTkLabel(master=equipment_frame, text="Weapon")
weapon_label.grid(pady=12, padx=15, row=1, column=0)
weapon_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="sword, shield...")
weapon_entry.grid(pady=12, padx=25, row=1, column=1)

chestarmor_label = customtkinter.CTkLabel(master=equipment_frame, text="Chest")
chestarmor_label.grid(pady=12, padx=15, row=2, column=0)
chestarmor_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="robe, shirt, tunic...")
chestarmor_entry.grid(pady=12, padx=25, row=2, column=1)

leggings_label = customtkinter.CTkLabel(master=equipment_frame, text="Legs")
leggings_label.grid(pady=12, padx=15, row=3, column=0)
leggings_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="pants, skirt...")
leggings_entry.grid(pady=12, padx=25, row=3, column=1)

helmet_label = customtkinter.CTkLabel(master=equipment_frame, text="Helmet")
helmet_label.grid(pady=12, padx=25, row=1, column=2)
helmet_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="hood, hat...")
helmet_entry.grid(pady=12, padx=45, row=1, column=3)

jewelry_label = customtkinter.CTkLabel(master=equipment_frame, text="Jewelery")
jewelry_label.grid(pady=12, padx=25, row=2, column=2)
jewelry_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="necklace, earings")
jewelry_entry.grid(pady=12, padx=25, row=2, column=3)

gloves_label = customtkinter.CTkLabel(master=equipment_frame, text="Gloves")
gloves_label.grid(pady=12, padx=25, row=3, column=2)
gloves_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="gloves, gauntlets...")
gloves_entry.grid(pady=12, padx=25, row=3, column=3)

boots_label = customtkinter.CTkLabel(master=equipment_frame, text="Boots")
boots_label.grid(pady=12, padx=15, row=4, column=0)
boots_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="boots, shoes...")
boots_entry.grid(pady=12, padx=25, row=4, column=1)

belt_label = customtkinter.CTkLabel(master=equipment_frame, text="Belt")
belt_label.grid(pady=12, padx=25, row=4, column=2)
belt_entry = customtkinter.CTkEntry(master=equipment_frame, placeholder_text="belt, waistband...")
belt_entry.grid(pady=12, padx=25, row=4, column=3)

#Button Functions to generate image from the entries above and save the image.
button = customtkinter.CTkButton(master=button_frame, text="Generate", command=generate_art)
button.grid(row=6, column=0, padx=10, sticky='we')

save_button = customtkinter.CTkButton(master=button_frame, text="Save Image", command=save_image)
save_button.grid(row=6, column=1, padx=10, sticky='we')

model_switch_button = customtkinter.CTkButton(master=button_frame, text="Switch Model", command=switch_model)
model_switch_button.grid(row=6, column=2, padx=10, sticky='we')

#GUI Mainloop
root.mainloop()