from flask import (
    Flask, 
    url_for,
    render_template,
    request,
    redirect,
    session,
    flash
)

app = Flask(__name__)
app.secret_key = 'FLHJK3678µ▒8U4☻'

@app.route('/')
def view_lyrics():
    # get text from text file
    lyrics_text = get_lyrics()
    return render_template('view_lyrics.html', lyrics=lyrics_text)

@app.route('/edit_lyrics', methods=['GET', 'POST'])
def edit_lyrics():
    if request.method == 'POST':
        # write text to text file
        write_lyrics(request.form['lyrics'])
        return redirect(url_for('edit_lyrics'))
    
    elif request.method == 'GET':
        # get text from text file
        lyrics_text = get_lyrics()
        return render_template('edit_lyrics.html', lyrics=lyrics_text)

def get_lyrics():
    with open('lyrics.txt', 'r', encoding='utf-8') as file:
        lyrics_text = file.readlines()
        lyrics_text = ''.join(lyrics_text)
        file.close()
        return lyrics_text
    
def write_lyrics(lyrics):
    with open('lyrics.txt', 'w') as file:
        file.write(lyrics)
        file.close()

if __name__ == '__main__':
    app.run(debug=True)