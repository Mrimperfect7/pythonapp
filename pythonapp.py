     from flask import Flask, request, send_file
     from gtts import gTTS
     from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
     import os

     app = Flask(__name__)

     @app.route('/convert', methods=['POST'])
     def convert_text_to_video():
         text = request.form['text']
         
         # Generate audio
         tts = gTTS(text)
         audio_file = 'output.mp3'
         tts.save(audio_file)
         
         # Load a background video (replace with your file)
         video = VideoFileClip('background.mp4').subclip(0, len(text)/10)  # Adjust duration
         
         # Combine
         audio = AudioFileClip(audio_file)
         final_video = video.set_audio(audio)
         final_video.write_videofile('output.mp4', fps=24)
         
         return send_file('output.mp4', as_attachment=True)

     if __name__ == '__main__':
         app.run()
     
