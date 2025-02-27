from moviepy.editor import VideoFileClip
import whisper
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from typing import List
from langchain.schema import Document
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


def load_text_file(file_path: str) -> List[Document]:
    loader = TextLoader(file_path,encoding='utf-8')
    return loader.load()

def load_document(file_path: str) -> List[Document]:
    if file_path.endswith('.txt'):
        return load_text_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    
def genarate_action_points(text_docs):
    # Extract the text content from the document
    response=llm.invoke(f'This is the transcript from the meeting {text_docs[0].page_content}. Can you generate the action points from this text.And keep focus on every small detail in the transcript.')
    action_points=(response.content)
    print(action_points)

    return action_points

def save_action_points(action_points,name):
    with open(f"{name}_action_points.md", "w",encoding='utf-8') as file:
        file.write(action_points)
    print("Action points saved to formatted_action_points.md")


def extract_audio_from_video(video_path, audio_output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)

def transcribe_audio(audio_path, model_size="base"):
       
    model = whisper.load_model(model_size)
        
        # Transcribe the audio
    result = model.transcribe(audio_path)
    return result['text']    
        
def save_transcript(transcript, output_file):
    """Save the transcript in a readable format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write plain text format
        f.write(transcript)

def video_to_text(output_text_path=None, model_size="base"):
    video_path="test_video.mp4"
    intermediate_audio_path = "extracted_audio.wav"
    print(video_path[:-4])
    output_text_path=f"{video_path[:-4]}_transcription.txt"

    extract_audio_from_video(video_path, intermediate_audio_path)
    result=transcribe_audio(intermediate_audio_path, model_size)
    save_transcript(result, output_text_path)
    if os.path.exists(intermediate_audio_path):
        os.remove(intermediate_audio_path)

    text_docs = load_document(output_text_path)
    action_points=genarate_action_points(text_docs)
    save_action_points(action_points,video_path[:-4])

    
    
def main():
    video_to_text(
        model_size="base")


if __name__ == "__main__":
    main()