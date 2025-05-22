# Video to Text Transcription and Action Points Generator

This project is a web application that converts video content into text transcripts and automatically generates action points from the content. It uses advanced AI models to provide accurate transcriptions and intelligent action point extraction.

## Features

- Video to text transcription using OpenAI's Whisper model
- Automatic action points generation using Google's Gemini AI
- Export action points in both Word (.docx) and PDF formats
- Web-based interface for easy file upload and processing
- Support for MP4 video files

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- Google API key for Gemini AI

## Installation

1. Clone the repository:
```bash
git https://github.com/huzaifa-khan-o16labs/Speech-To-Text
cd Speech-To-Text
```

2. Create and activate a virtual environment:
```bash
python -m venv env
# On Windows
env\Scripts\activate
# On Unix or MacOS
source env/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask application:
```bash
python script.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload your video file through the web interface

4. The system will:
   - Extract audio from the video
   - Transcribe the audio to text
   - Generate action points
   - Create downloadable Word and PDF documents

5. Download the generated action points in your preferred format

## Project Structure

```
├── script.py              # Main application file
├── requirements.txt       # Python dependencies
├── .env_example.txt      # Example environment variables
├── templates/            # HTML templates
├── ffmpeg/              # FFmpeg binaries
└── env/                 # Virtual environment
```

## Dependencies

The project uses several key libraries:
- Flask: Web framework
- Whisper: Speech recognition
- Google Generative AI: Action points generation
- MoviePy: Video processing
- python-docx: Word document generation
- FPDF: PDF generation

## Notes

- The transcription quality depends on the audio quality of the input video
- Processing time may vary based on video length and system specifications
- Make sure to keep your API keys secure and never commit them to version control
