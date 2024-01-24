import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_folder='static')

data = []

def veriAl():
    global data
    with sqlite3.connect('Project.db') as con:
        cur = con.cursor()
        cur.execute("select * from Projects")
        data = cur.fetchall()
        for project in data:
           print(project)
               

@app.route("/index")
def index():
    veriAl()
    return render_template("index.html", data=data)

@app.route("/lupa")
def lupa():
    return render_template("Lupa.html")

@app.route("/AutoMotive")
def automotive():
    return render_template("AutoMotive.html")

@app.route("/wordrem")
def wordrem():
    return render_template("WordRem.html")

@app.route('/proje_ekle_sayfasi')
def proje_ekle_sayfasi():
    return render_template('ProjeEkle.html')

@app.route('/proje_ekle', methods=['POST'])
def proje_ekle():
    if request.method == 'POST':
        proje_adi = request.form['projeAdi']
        proje_aciklama = request.form['projeAciklama']

        # Burada veritabanına proje eklemesi yapılmalıdır.
        # Örnek olarak bir SQLite veritabanı kullanıldığını varsayalım:
        # Bu kısmı kendi veritabanı yapınıza göre uyarlamalısınız.
        with sqlite3.connect('Project.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Projects (name, description) VALUES (?, ?)", (proje_adi, proje_aciklama))
            con.commit()

    return redirect(url_for('index'))  # Proje ekledikten sonra ana sayfaya yönlendir.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

