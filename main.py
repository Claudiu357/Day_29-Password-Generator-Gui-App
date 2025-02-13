from  tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock_img)
canvas.grid(row=0, column= 1)

website_label = Label(text="Website:   ")
website_label.grid(row=1, column=0)

web_input = Entry(width=52)
web_input.grid(row=1, column= 1, columnspan = 2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column = 0)

email_username_input = Entry(width=52)
email_username_input.grid(row = 2, column= 1, columnspan = 2)

password_label = Label(text = "Password:  ")
password_label.grid(row=3,column=0)

password_input = Entry(width=33)
password_input.grid(row = 3, column = 1)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column= 2)

add_button = Button(text="Add", width=44)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()
