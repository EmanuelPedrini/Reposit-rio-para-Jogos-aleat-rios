import random; import sys; import tkinter
def rolld20():
    return random.randint(1,20)
print("Welcome to retroquest! if want to stop the game, type [EXIT] ")
root = tk.Tk()
root.title("Janela")
root.configure(bg="black")

text = tk.Text(
    root,
    bg="black",
    fg="white",
    insertbackground="white",
    font=("Consolas", 14)
)
text.pack(expand=True, fill="both")

class Redirect:
    def write(self, msg):
        text.insert("end", msg)
        text.see("end")
    def flush(self):
        pass

sys.stdout = Redirect()

print("Janela funcionando")
print("Tudo que você printar aparece aqui")

root.mainloop()

personagem={
    "name" : "guerreiro",
    "acthealth" : 3,
    "maxhealth": 3
    }
print(personagem["name"])
