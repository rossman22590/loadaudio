# LoadAudioFromURL - ComfyUI Custom Node

**Load audio directly from URLs into ComfyUI workflows with zero hassle.**

A lightweight, production-ready custom node that downloads and processes audio files from any HTTP/HTTPS URL, returning them in ComfyUI's native audio format. Perfect for workflows that need remote audio sources, streaming content, or dynamic audio loading.

---

## ✨ Features

- 🌐 **Load from any URL** - HTTP/HTTPS support with automatic download
- 🎵 **Multi-format support** - WAV, MP3, FLAC, OGG, AIFF, and more
- 🔄 **Mono/Stereo handling** - Automatically detects and converts
- ⏱️ **Frame capping** - Limit audio length for memory efficiency
- 🛡️ **Robust error handling** - Clear error messages, no silent failures
- 🧹 **Auto cleanup** - Temporary files removed automatically
- ⚡ **Fast & lightweight** - Minimal dependencies, optimized for speed
- 🔗 **Full compatibility** - Works with all ComfyUI audio nodes

---

## 📦 Installation

### Quick Install (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/audionode.git
cd audionode
pip install -r requirements.txt
```

Restart ComfyUI. Done! ✅

### Manual Install

1. Download the `audionode` folder
2. Place it in `ComfyUI/custom_nodes/audionode/`
3. Run: `pip install -r ComfyUI/custom_nodes/audionode/requirements.txt`
4. Restart ComfyUI

---

## 🚀 Quick Start

### Basic Usage

1. Add **"Load Audio From URL"** node to your workflow
2. Paste your audio URL
3. Connect to any audio processing node
4. Run!

### Example URLs

```
https://example.com/audio.wav
https://cdn.example.com/music.mp3
https://storage.example.com/podcast.flac
```

---

## 📋 Node Documentation

### Inputs

| Input | Type | Description | Default |
|-------|------|-------------|---------|
| **url** | STRING | Direct URL to audio file | Required |
| **frame_load_cap** | INT | Max duration in seconds (0 = unlimited) | 0 |

### Outputs

| Output | Type | Description |
|--------|------|-------------|
| **AUDIO** | AUDIO | ComfyUI audio object (waveform + sample rate) |

### Output Format

```python
{
    "waveform": torch.Tensor,  # Shape: (channels, samples)
    "sample_rate": int         # Hz (e.g., 44100, 48000)
}
```

---

## 💡 Usage Examples

### Example 1: Load a Simple Audio File

```
URL: https://example.com/background-music.wav
Frame Load Cap: 0 (load entire file)
```

### Example 2: Load with Duration Limit

```
URL: https://example.com/long-podcast.mp3
Frame Load Cap: 30 (load first 30 seconds)
```

### Example 3: Chain with Audio Processing

```
LoadAudioFromURL → Audio Processing Node → Save Audio
```

---

## 🎯 Supported Audio Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| WAV | `.wav` | ✅ Full support |
| MP3 | `.mp3` | ✅ Requires ffmpeg |
| FLAC | `.flac` | ✅ Full support |
| OGG | `.ogg` | ✅ Full support |
| AIFF | `.aiff`, `.aif` | ✅ Full support |
| M4A | `.m4a` | ⚠️ Requires ffmpeg |
| WMA | `.wma` | ⚠️ Requires ffmpeg |

---

## ⚙️ Requirements

### Core Dependencies

- Python 3.8+
- numpy >= 1.21.0
- soundfile >= 0.12.1
- torch (usually already installed with ComfyUI)

### Optional Dependencies

For MP3 and other compressed formats:

**Windows:**
```bash
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

---

## 🔧 Troubleshooting

### ❌ "soundfile not found"

**Solution:**
```bash
pip install soundfile
```

### ❌ "MP3 format not supported"

**Solution:** Install ffmpeg (see Requirements section above)

### ❌ "Failed to download audio from URL"

**Possible causes:**
- URL is incorrect or typo
- File doesn't exist at that URL
- Network connectivity issue
- URL requires authentication
- Server blocks automated downloads

**Solution:**
- Verify URL works in browser
- Check network connection
- Try a different URL
- Some servers may require User-Agent headers (contact support)

### ❌ "URL cannot be empty"

**Solution:** Make sure you've entered a URL in the node

### ❌ "Memory error" or "Out of memory"

**Solution:** Use `frame_load_cap` to limit audio length:
```
frame_load_cap: 60  # Load only first 60 seconds
```

### ❌ Node doesn't appear in ComfyUI

**Solution:**
1. Check folder is at `ComfyUI/custom_nodes/audionode/`
2. Verify `__init__.py` exists
3. Check ComfyUI console for errors
4. Restart ComfyUI completely
5. Clear browser cache (Ctrl+Shift+Delete)

---

## 📊 Performance Tips

### For Large Files

Use `frame_load_cap` to load only what you need:

```python
# Load only first 2 minutes instead of entire 1-hour file
frame_load_cap: 120
```

### For Batch Processing

Download files once, then reference locally:

```python
# First run: Load from URL
URL: https://example.com/audio.wav

# Subsequent runs: Load from local file
# (Use ComfyUI's built-in LoadAudio node)
```

### For Streaming Workflows

Keep URLs accessible and use reasonable frame caps to avoid memory issues.

---

## 🔐 Security Notes

- ✅ Only downloads from URLs you explicitly provide
- ✅ Temporary files are automatically deleted
- ✅ No data is sent anywhere except to the URL you specify
- ⚠️ Be cautious with untrusted URLs
- ⚠️ Large files will consume disk space temporarily

---

## 🤝 Compatibility

### Works With

- ✅ All ComfyUI audio processing nodes
- ✅ Audio visualization nodes
- ✅ Audio encoding/saving nodes
- ✅ Custom audio nodes
- ✅ ComfyUI Manager

### Tested On

- ComfyUI (latest)
- Python 3.8, 3.9, 3.10, 3.11
- Windows, macOS, Linux

---

## 📝 Examples & Workflows

### Workflow 1: Load & Save Audio

```
LoadAudioFromURL → Save Audio (MP3)
```

### Workflow 2: Load & Process

```
LoadAudioFromURL → Audio Effects → Save Audio
```

### Workflow 3: Load with Duration Limit

```
LoadAudioFromURL (frame_load_cap: 30) → Audio Processing → Output
```

---

## 🐛 Bug Reports & Feature Requests

Found an issue? Have a suggestion?

1. Check the Troubleshooting section above
2. Check existing GitHub issues
3. Create a new issue with:
   - Error message (from console)
   - URL you're trying to load
   - Your system info (OS, Python version)
   - Steps to reproduce

---

## 📄 License

MIT License - Feel free to use, modify, and distribute

---

## 🙏 Credits

Built for ComfyUI community. Uses:
- **soundfile** - Audio file I/O
- **numpy** - Numerical operations
- **torch** - Tensor operations

---

## 💬 Support

**Having issues?**

1. Check the Troubleshooting section
2. Review the Examples section
3. Check ComfyUI console for detailed error messages
4. Create a GitHub issue with error details

**Want to contribute?**

Pull requests welcome! Please include:
- Description of changes
- Testing results
- Any new dependencies

---

## 🎯 Roadmap

- [ ] Batch URL loading
- [ ] Audio format conversion
- [ ] Caching support
- [ ] Proxy support
- [ ] Authentication support

---

**Made with ❤️ for the ComfyUI community**

Questions? Issues? Suggestions? Open an issue on GitHub!
