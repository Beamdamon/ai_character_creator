import torch
from diffusers import StableDiffusionPipeline
from diffusers.pipelines.stable_diffusion.convert_from_ckpt import download_from_original_stable_diffusion_ckpt

#Sets the diffusion model from the pretrained model. Safety Chekcer disables the safety checker to prevent from being blacked out. NSFW images are turned off in the negative prompt.
modelname = "Lykon/NeverEnding-Dream"
pipe = StableDiffusionPipeline.from_pretrained(modelname, torch_dtype=torch.float16, safety_checker = None) #Good for photorealistic / digital art / anime / allrounder
#pipe2 = StableDiffusionPipeline.from_pretrained("Ojimi/anime-kawai-diffusion", torch_dtype=torch.float16, safety_checker = None) #Good for very anime art style

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
c_class = ''
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