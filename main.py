from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask("__name__")


@app.route("/")
def main():
  return render_template("main.html")


@app.route("/mp4", methods=["GET"])
def mp4():
  if request.method == "GET":
    if request.args.get("highres") == "on":
      v = request.args.get("v")
      yt = YouTube(v)
      yt.streams.filter(
        progressive=True,
        file_extension="mp4").get_highest_resolution().download(
          filename=f'{yt.title}.mp4')
      file = f'{yt.title}.mp4'
      return send_file(file, as_attachment=True)
    else:
      v = request.args.get("v")
      yt = YouTube(v)
      yt.streams.filter(progressive=True,
                        file_extension="mp4").get_lowest_resolution().download(
                          filename=f'{yt.title}.mp4')
      file = f'{yt.title}.mp4'
      return send_file(file, as_attachment=True)


@app.route("/mp3", methods=["GET"])
def mp3():
  if request.method == "GET":
    v = request.args.get("v")
    yt = YouTube(v)
    yt.streams.filter(only_audio=True).first().download(
      filename=f'{yt.title}.mp3')
    file = f'{yt.title}.mp3'
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=False)
