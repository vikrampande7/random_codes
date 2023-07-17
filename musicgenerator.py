import jukebox
import torch as t
from jukebox.make_models import make_vqvae, make_prior, make_flow, make_vae
from jukebox.hparams import Hyperparams, setup_hparams
from jukebox.sample import sample_single_window

# Load the Jukebox model
hparas = Hyperparams()
hps = setup_hparams(hparas)
vqvae = make_vqvae(hps)
prior = make_prior(hps)
flow = make_flow(hps, prior)

# Load the genre condition tokens
genre_dict = {"rock": 0, "pop": 1, "jazz": 2}

genre = "rock"
genre_token = genre_dict[genre]

# Sample 5 seconds of music
duration = 5
samples = sample_single_window(prior, flow, vqvae, hps, cond=[genre_token],
                              sampling_kwargs={"temp":1.0}, duration=duration)

# Save the generated wav
jukebox.utils.audio_utils.save_wav(samples, f"{genre}_sample.wav", sr=22050)

