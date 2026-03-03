import os
import urllib.request
import tempfile
import numpy as np
import soundfile as sf
from pathlib import Path

class LoadAudioFromURL:
    """
    Load audio from a URL and convert it to ComfyUI's audio format.
    Returns audio in the same format as ComfyUI's LoadAudio node.
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "url": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
            },
            "optional": {
                "frame_load_cap": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 2147483647,
                    "step": 1,
                    "display": "number"
                }),
            }
        }
    
    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("AUDIO",)
    FUNCTION = "load_audio"
    CATEGORY = "audio"
    
    def load_audio(self, url, frame_load_cap=0):
        """
        Load audio from URL and return in ComfyUI format.
        
        Returns:
            tuple: ({"waveform": tensor, "sample_rate": int},)
        """
        
        if not url or url.strip() == "":
            raise ValueError("URL cannot be empty")
        
        # Create temporary file to download audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_path = tmp_file.name
        
        try:
            # Download audio from URL
            print(f"Downloading audio from: {url}")
            urllib.request.urlretrieve(url, tmp_path)
            
            # Load audio using soundfile
            audio_data, sample_rate = sf.read(tmp_path)
            
            # Handle mono/stereo
            if len(audio_data.shape) == 1:
                # Mono - reshape to (1, samples)
                audio_data = audio_data.reshape(1, -1)
            else:
                # Stereo or multi-channel - transpose to (channels, samples)
                audio_data = audio_data.T
            
            # Apply frame load cap if specified
            if frame_load_cap > 0:
                max_frames = frame_load_cap * sample_rate
                if audio_data.shape[1] > max_frames:
                    audio_data = audio_data[:, :max_frames]
                    print(f"Audio capped to {frame_load_cap} seconds")
            
            # Convert to float32 and normalize to [-1, 1] range
            audio_data = audio_data.astype(np.float32)
            
            # Normalize if needed
            max_val = np.max(np.abs(audio_data))
            if max_val > 1.0:
                audio_data = audio_data / max_val
            
            # Convert to torch tensor
            import torch
            waveform = torch.from_numpy(audio_data).unsqueeze(0)  # Add batch dimension
            
            print(f"Audio loaded successfully. Sample rate: {sample_rate}, Shape: {waveform.shape}")
            
            return ({"waveform": waveform, "sample_rate": sample_rate},)
        
        except urllib.error.URLError as e:
            raise ValueError(f"Failed to download audio from URL: {e}")
        except Exception as e:
            raise ValueError(f"Failed to load audio: {e}")
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except:
                    pass


# Node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "LoadAudioFromURL": LoadAudioFromURL
}

# Display names in the UI
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadAudioFromURL": "Load Audio From URL"
}
