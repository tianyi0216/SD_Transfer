## SD Transfer


### Description

This is the repository for a large course project for STAT 453 Deep Learning at UW-Madison.

We finetuned a conditioned diffusion model guided by text prompts to accomplish style transfer on images. We largely utilized the pretrained image editing model instructPix2Pix, which can be found at https://github.com/timothybrooks/instruct-pix2pix. We also used the StableDiffusion 1.5, and HuggingFace for their API to access and train these models.

### Explanation of Files

- `finetune_instruct_pix2pix.py` and `train_instruct_pix2pix.py` contains the code from HuggingFace to finetune the instructPix2Pix model, with some modifications to accomplish for our needs.
- `finetune_model.ipynb` contains the code of how we finetuned the instructPix2Pix model.
- `Evaluate.ipynb` contains the code of how we evaluated the model according to the experiment section of the report.
- `clip_sim.ipynb` contains the code for plotting the clip similarity of the generated images with target images.
- `dir_sim.ipynb` contains the code for plotting the direction similarity of the change with the target image.
- `data` directory contains the code we used to generate the dataset.