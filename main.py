import customtkinter, ctypes

windowVelocity = 1
windowAcceleration = 0.1
Up = False
Stop = False
Bounces = 0

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

def Gravity():
    global windowVelocity, windowAcceleration, Up, Stop, Bounces

    if Stop:
        windowVelocity = 0
    else:
        if Up:
            windowVelocity *= -0.8 + Bounces * 0.02
            windowVelocity = -abs(windowVelocity)
            if windowVelocity < -1e-10:
                Bounces += 1
                Up = False
        else:
            windowVelocity += windowAcceleration

    xPos = root.winfo_x()
    yPos = root.winfo_y()

    if yPos + windowVelocity > 408:
        yPos = 408
        Up = True

    if abs(windowVelocity) > 0.01:
        root.geometry(f'{x}x{y}+{xPos}+{yPos+windowVelocity}')
    root.after(1, Gravity)

def drawCube(Canvas):
    Scale = 0.7

    xOffset = 100
    yOffset = 200

    # Front Square
    F_TL = ((210+xOffset)*Scale, (290-yOffset)*Scale)
    F_TR = ((435+xOffset)*Scale, (360-yOffset)*Scale)
    F_BL = ((250+xOffset)*Scale, (545-yOffset)*Scale)
    F_BR = ((430+xOffset)*Scale, (700-yOffset)*Scale)

    # Back Square
    B_TL = ((430+xOffset)*Scale, (260-yOffset)*Scale)
    B_TR = ((655+xOffset)*Scale, (290-yOffset)*Scale)
    B_BR = ((610+xOffset)*Scale, (550-yOffset)*Scale)

    # Shading
    Canvas.create_polygon([F_TR, B_TR, B_BR, F_BR], fill='#B300B3')
    Canvas.create_polygon([B_TL, B_TR, F_TR, F_TL], fill='#FF00FF')
    Canvas.create_polygon([F_TL, F_TR, F_BR, F_BL], fill='#610061')

x, y = 600, 600

root = customtkinter.CTk()
root.geometry(f'{x}x{y}')
root.title('Main')

Canvas = customtkinter.CTkCanvas(root, width=screensize[0], height=screensize[1], highlightbackground='gray14', bg='gray14')
Canvas.pack()

Button = customtkinter.CTkButton(root, text='Apply gravity to cube', command=Gravity, fg_color='#800080', text_color='white')
Button.place(x=30, y=50)


drawCube(Canvas)

root.mainloop()
