import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

window = Tk()

window.geometry("640x480")
window.configure(bg = "#10640c")
canvas = Canvas(
    window,
    bg = "#10640c",
    height = 480,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    309.5, 240.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    332.0, 126.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 209.0, y = 111,
    width = 246.0,
    height = 28)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    332.0, 284.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 214.0, y = 195,
    width = 236.0,
    height = 177)

def btn_clicked():

    navegador = webdriver.Chrome()

    numero = entry0.get()
    mensagem = str(entry1.get("1.0", END).strip())
    navegador.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")

    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2)

    navegador.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span/div/div[2]/div[2]/button").send_keys(Keys.ENTER)
    time.sleep(5)

print("Mensagem Enviada!")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 132, y = 409,
    width = 400,
    height = 42)

window.resizable(False, False)
window.mainloop()
