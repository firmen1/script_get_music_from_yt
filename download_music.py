from pytube import YouTube
import os

def download_audio(url, output_path='music_folder'):
    try:
        yt = YouTube(url)

        audio_stream = yt.streams.filter(only_audio=True).first()

        audio_stream.download(output_path)

        print(f"Audio downloaded successfully: {yt.title}")
    except Exception as e:
        print(f"Error: {str(e)}")

def get_link(note_path):
  links = []
  try:
      with open(note_path, 'r') as file:
          lines = file.readlines()

          for line in lines:
              links.append(line.strip())
  except FileNotFoundError:
      print(f"File not found: {note_path}")
  except Exception as e:
      print(f"Error: {str(e)}")
  return links

def main():
  n_path = 'link.txt'
  links = get_link(n_path)
  for link in links:
    download_audio(link)
if __name__ == "__main__":
    main()
