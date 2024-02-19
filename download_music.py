from pytube import YouTube
import yt_dlp
import os

def download_video_to_mp3(url, output_path='music_folder'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': "C:/ffmpeg/bin",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Video downloaded and converted to MP3 successfully.")
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
    music_dir_path = 'music_folder'
    links = get_link(n_path)
    for link in links:
        download_video_to_mp3(link, music_dir_path)

if __name__ == "__main__":
    main()
