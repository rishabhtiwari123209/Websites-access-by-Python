
from tkinter import *
import webbrowser
##

def data():

    Label(root1, text="social media", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=0, column=2, padx=10)
    b1 = Button(root1, text="what app", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://web.whatsapp.com/")).grid(row=1, column=0, padx=10, pady=20)
    b2 = Button(root1, text="facebook", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.facebook.com/")).grid(row=1, column=1, padx=10, pady=20)
    b2 = Button(root1, text="twitter", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://twitter.com/")).grid(row=1, column=2, padx=10, pady=20)
    b2 = Button(root1, text="youtube", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.youtube.com/")).grid(row=1, column=3, padx=10, pady=20)
    b2 = Button(root1, text="pinterest", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.pinterest.com/")).grid(row=1, column=4, padx=10, pady=20)
    b2 = Button(root1, text="instagram", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.instagram.com/?hl=en")).grid(row=1, column=5, padx=10, pady=20)
    b2 = Button(root1, text="tiktok", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.tiktok.com/en/")).grid(row=1, column=6, padx=10, pady=20)
    # =============================
    Label(root1, text="BANKING", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=2, column=2, padx=10)

    b1 = Button(root1, text="allahabad", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.allahabadbank.com/")).grid(row=3, column=0, padx=10, pady=20)
    b2 = Button(root1, text="axis ", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.axisbank.com/")).grid(row=3, column=1, padx=10, pady=20)
    b2 = Button(root1, text="canara", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.canarabank.com/")).grid(row=3, column=2, padx=10, pady=20)
    b2 = Button(root1, text="icici", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.icicibank.com/")).grid(row=3, column=3, padx=10, pady=20)
    b2 = Button(root1, text="sbi", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.sbi.co.in/")).grid(row=3, column=4, padx=10, pady=20)
    b2 = Button(root1, text="hdfc", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.hdfcbank.com/")).grid(row=3, column=5, padx=10, pady=20)
    b2 = Button(root1, text="bankOfB", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.bankofindia.com/")).grid(row=3, column=6, padx=10, pady=20)
    # ,pady=20

    Label(root1, text="SHOPPING", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=4, column=2, padx=10)

    b1 = Button(root1, text="amazon", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.amazon.in/")).grid(row=6, column=0, padx=10, pady=20)
    b2 = Button(root1, text="flipkart", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.flipkart.com/")).grid(row=6, column=1, padx=10, pady=20)
    b2 = Button(root1, text="http", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("")).grid(row=6, column=2, padx=10, pady=20)
    b2 = Button(root1, text="myntra", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.myntra.com/")).grid(row=6, column=3, padx=10, pady=20)
    b2 = Button(root1, text="snapdeal", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.snapdeal.com/")).grid(row=6, column=4, padx=10, pady=20)
    b2 = Button(root1, text="", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.ebay.com/")).grid(row=6, column=5, padx=10, pady=20)
    b2 = Button(root1, text="yo", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("")).grid(row=6, column=6, padx=10, pady=20)
    # =============================
    Label(root1, text="SONGS", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=7, column=2, padx=10)

    b1 = Button(root1, text="gaana", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://gaana.com/")).grid(row=8, column=0, padx=10)
    b2 = Button(root1, text="wynk", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://wynk.in/music")).grid(row=8, column=1, padx=10)
    b2 = Button(root1, text="jiosaavn", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.jiosaavn.com/")).grid(row=8, column=2, padx=10)
    b2 = Button(root1, text="pagalword", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.pagalworld.pw/")).grid(row=8, column=3, padx=10)
    b2 = Button(root1, text="free mp3download", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://free-mp3-download.net/")).grid(row=8, column=4, padx=10)
    b2 = Button(root1, text="mr-jatt", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://mr-jattt.net/")).grid(row=8, column=5, padx=10)
    b2 = Button(root1, text="yo", bg="yellow", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("")).grid(row=8, column=6, padx=10)
    # we2
    Label(root1, text="social media", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=9, column=2, padx=10)
    b1 = Button(root1, text="what app", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("")).grid(row=10, column=0, padx=10, pady=20)
    b2 = Button(root1, text="facebook", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.edx.org/")).grid(row=10, column=1, padx=10, pady=20)
    b2 = Button(root1, text="twitter", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://en.wikipedia.org/wiki/Main_Page")).grid(row=10, column=2, padx=10, pady=20)
    b2 = Button(root1, text="youtube", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("")).grid(row=10, column=3, padx=10, pady=20)
    b2 = Button(root1, text="pinterest", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("ht")).grid(row=10, column=4, padx=10, pady=20)
    b2 = Button(root1, text="instagram", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://")).grid(row=10, column=5, padx=10, pady=20)
    b2 = Button(root1, text="tiktok", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.khanacademy.org/")).grid(row=10, column=6, padx=10, pady=20)
    # =============================
    Label(root1, text="COMPUTER INFO.", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=11, column=2, padx=10)

    b1 = Button(root1, text="tutorial", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.tutorialspoint.com/")).grid(row=12, column=0, padx=10, pady=20)
    b2 = Button(root1, text="greekForGreek", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.geeksforgeeks.org/")).grid(row=12, column=1, padx=10, pady=20)
    b2 = Button(root1, text="studyTonight", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.studytonight.com/")).grid(row=12, column=2, pady=20)
    b2 = Button(root1, text="w3school", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.w3schools.com/")).grid(row=12, column=3, padx=10, pady=20)
    b2 = Button(root1, text="quora", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.quora.com/")).grid(row=12, column=4, padx=10, pady=20)
    b2 = Button(root1, text="stackOverflow", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://stackoverflow.com/")).grid(row=12, column=5, padx=10, pady=20)
    b2 = Button(root1, text="javaPoint", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.javatpoint.com/")).grid(row=12, column=6, padx=10, pady=20)
    # ,pady=20

    Label(root1, text="CERTIFICATION ", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=13, column=2, padx=10)

    b1 = Button(root1, text="certificate.google", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://grow.google/certificates/")).grid(row=14, column=0, padx=10, pady=20)
    b2 = Button(root1, text="udemy", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.udemy.com/topic/computer-skills/")).grid(row=14, column=1, padx=10, pady=20)
    b2 = Button(root1, text="cousera", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("http://www.cousera.org/")).grid(row=14, column=2, padx=10, pady=20)
    b2 = Button(root1, text="codechef", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.codechef.com/")).grid(row=14, column=3, padx=10, pady=20)
    b2 = Button(root1, text="hackerrank", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.hackerrank.com/")).grid(row=14, column=4, padx=10, pady=20)
    b2 = Button(root1, text="topCoder", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.topcoder.com/")).grid(row=14, column=5, padx=10, pady=20)
    b2 = Button(root1, text="coderbyte", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://coderbyte.com/")).grid(row=14, column=6, padx=10, pady=20)
    # =============================https://duckduckgo.com/
    Label(root1, text="NEWS AND ENGINE", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=15, column=2, padx=10)
    b1 = Button(root1, text="indiaToday", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.indiatoday.in/news.html")).grid(row=16, column=0, padx=10)
    b2 = Button(root1, text="thehindu", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.thehindu.com/news/")).grid(row=16, column=1, padx=10)
    b2 = Button(root1, text="bhaskar", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.bhaskar.com/")).grid(row=16, column=2, padx=10)
    b2 = Button(root1, text="ndtv", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://ndtv.in/")).grid(row=16, column=3, padx=10)
    b2 = Button(root1, text="abplive", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.abplive.com/")).grid(row=16, column=4, padx=10)
    b2 = Button(root1, text="bing", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.bing.com/")).grid(row=16, column=5, padx=10)
    b2 = Button(root1, text="duckduckgo", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://duckduckgo.com/")).grid(row=16, column=6, padx=10)
  # =============================https://duckduckgo.com/
    Label(root1, text="NEWS AND ENGINE", bg="black", fg="aqua", font="comicsansms 20 bold",
          borderwidth=3, relief=GROOVE).grid(row=17, column=2, padx=10)
    b1 = Button(root1, text="indiaToday", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.indiatoday.in/news.html")).grid(row=18, column=0, padx=10)
    b2 = Button(root1, text="thehindu", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.thehindu.com/news/")).grid(row=18, column=1, padx=10)
    b2 = Button(root1, text="bhaskar", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.bhaskar.com/")).grid(row=16, column=2, padx=10)
    b2 = Button(root1, text="ndtv", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://ndtv.in/")).grid(row=16, column=3, padx=10)
    b2 = Button(root1, text="abplive", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.abplive.com/")).grid(row=16, column=4, padx=10)
    b2 = Button(root1, text="bing", bg="orange", fg="black", font="comicsansms 15", borderwidth=1, relief=GROOVE,
                command=lambda: webbrowser.open_new("https://www.bing.com/")).grid(row=16, column=5, padx=10)
    b2 = Button(root1, text="duckduckgo", bg="orange", fg="black", font="comicsansms 15", borderwidth=1,
                relief=GROOVE, command=lambda: webbrowser.open_new("https://duckduckgo.com/")).grid(row=16, column=6, padx=10)

    b2 = Button(root, text="QUIT", bg="black", fg="aqua", font="comicsansms 17 bold",
                borderwidth=3, relief=GROOVE, command=lambda: root.destroy()).pack(side=BOTTOM)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=1250, height=650)


root = Tk()
root.geometry("1300x650")
f = Frame(root, bg="aqua")
f.place(x=0, y=0, height=70, width=1300)

Label(f, text="WEBSITES", bg="black", fg="aqua", font="comicsansms 30 bold",
      borderwidth=3, relief=GROOVE).place(x=400, y=20)
Label(f, text="scroll down ", bg="black", fg="aqua",
      font="comicsansms 13").place(x=1000, y=50)

myframe = Frame(root, relief=GROOVE, width=1250, height=650, bd=1)
myframe.place(x=0, y=70)

canvas = Canvas(myframe)
root1 = Frame(canvas, bg="gray")
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=root1, anchor='nw')
root1.bind("<Configure>", myfunction)
data()
root.mainloop()
