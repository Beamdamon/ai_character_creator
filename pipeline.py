import torch
from diffusers import StableDiffusionPipeline


# comments - name, assignment, estimate, actual
#Damon Beam - Final Project - Expected time 25 hours - Actual time: 30 hours
#Uses models from HuggingFace to create AI generated characters. Uses the customTkinter UI for GUI. Project was a lot of fun to do, a lot of the time taken was learning how to
#use stable diffusion, finding good models, creating the ui, and learning how to best make art utilizing stable difusion's prompt system. I had a few bugs / misteps along the 
#way that also took some time to fix. Overall, I ran over the expected time, but I learned a ton about AI art and how to get the best results.


#Sets the diffusion model from the pretrained model. Safety Chekcer disables the safety checker to prevent from being blacked out. NSFW images are turned off in the negative prompt.
modelname = "Lykon/NeverEnding-Dream"
pipe = StableDiffusionPipeline.from_pretrained(modelname, torch_dtype=torch.float16) #Good for photorealistic / digital art / anime / allrounder
#pipe2 = StableDiffusionPipeline.from_pretrained("Ojimi/anime-kawai-diffusion", torch_dtype=torch.float16) #Good for very anime art style

#Uses"cuda" or the GPU. If set to "cpu" it can be ran on a cpu instead. Torch will need to be installed @ https://pytorch.org/get-started/locally/ based on the user's system.
pipe = pipe.to("cuda")


#Image Parameters
height = 512 #Height of image. Must be divisible by 8. 512 is default.
width = 512  #Width of image. Must be divisible by 8. 512 is default.
num_inference_steps = 80 #Number of steps for denoising. More stops causes longer generation time. 50 is default but higher can improve quality.
guidance_scale = 12 #Higher number give higher details but less diversity, lower numbers are more diverse but less detailed. Default is 7.5. Recommneded is 7.5-8.5.

#Art Characteristics 
medium = '' #illustration, oil painting, 3D Rendering, photography, digital painting, 
style = '' #artistic style
artist = '' #specific artists will give art in the style of their work
lighting = '' #changes the lighting of the art
image_color = '' #adds a color theme to the art
additional_details = '' #Any other detials not mentioned

#Physical Character Characteristics
gender = ''
race = ''
skin = ''
build = ''
height = ''
c_class = '' #Character class (mage, warrior, paladin, etc...)
hair = ''
eyes = ''
head = ''
face = ''
nose = ''
mouth = ''
ears = ''
pose = ''

#Character Equipment
weapon = ''
chestarmor = ''
leggings = ''
gloves = ''
boots = ''
helmet = ''
belt = ''
jewlery = ''


#Gernerator if using a manual seed.
#generator = [torch.Generator(device='cuda').manual_seed(132340231)]