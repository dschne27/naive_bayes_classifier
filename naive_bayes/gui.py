train_x = [['friend','good','good','bad','excellent','now'],
            ['worst','good','alright','bad','poor','no'],
            ['yes','great','help','now','excellent','alright'],
            ['indeed','good','work','bad','ok','better'],
            ['great','great','fantastic','bad','excellent','good'],
            ['alright','ok','wow','indeed','help','ok'],
            ['friend','poor','worst','bad','improvement','wow'],
            ['friend','good','good','better','strange','improvement'],
            ['great','good','work','bad','no','wow'],
            ]
train_y = [['positive'],
            ['negative'],
            ['neutral'],
            ['neutral'],
            ['positive'],
            ['neutral'],
            ['negative'],
            ['positive'],
            ['positive']]

test_y = [['positive'],
            ['negative'],
            ['neutral'],
            ['neutral'],
            ['positive'],
            ['neutral'],
            ['negative'],
            ['positive'],
            ['positive']]

test_x = [['friend','good','good','bad','excellent','now'],
            ['worst','good','alright','bad','poor','no'],
            ['yes','great','help','now','excellent','alright'],
            ['indeed','good','work','bad','ok','better'],
            ['great','great','fantastic','bad','excellent','good'],
            ['alright','ok','wow','indeed','help','ok'],
            ['friend','poor','worst','bad','improvement','wow'],
            ['friend','good','good','better','strange','improvement'],
            ['great','good','work','bad','no','wow'],
            ]

nb = NaiveBayes()

# nb.fit(train_x,train_y)
# nb.predict(train_x,test_y)
HEIGHT = 800
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#F0E998')
frame.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.7)

button = tk.Button(frame, text='Test button',bg='#F0E998')
button.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)

label = tk.Label(frame, text='This is a label',bg='pink')
label.place(relx = 0.01,rely=0.01,relwidth=0.98,relheight=0.05)
entry = tk.Entry(frame, bg='#6159D9')
entry.place(relx=0.25,rely=0.75,relwidth=0.7,relheight=0.7)

root.mainloop()