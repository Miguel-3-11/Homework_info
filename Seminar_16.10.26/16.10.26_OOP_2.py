from random import randrange as rnd, choice
from tkinter import Tk, Canvas, BOTH
import math

W, H = 800, 600
GX, GY = 40, 550
GRAVITY = 0.35
REST = 0.75


root = Tk()
root.geometry(f'{W}x{H}')
root.title('Пушка')
canv = Canvas(root, bg='white', width=W, height=H)
canv.pack(fill=BOTH, expand=1)


class Ball:
    """Класс Ball описывает мяч."""

    def __init__(self, x=GX, y=GY):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0.0
        self.vy = 0.0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r,
                                   self.x + self.r, self.y + self.r,
                                   fill=self.color, outline='')
        self.live = 200

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r,
                    self.x + self.r, self.y + self.r)

    def move(self):
        self.vy += GRAVITY

        self.x += self.vx
        self.y += self.vy

        if self.x - self.r < 0:
            self.x = self.r
            self.vx = abs(self.vx) * REST
        elif self.x + self.r > W:
            self.x = W - self.r
            self.vx = -abs(self.vx) * REST

        if self.y - self.r < 0:
            self.y = self.r
            self.vy = abs(self.vy) * REST

        if self.y + self.r > H:
            self.y = H - self.r
            self.vy = -abs(self.vy) * REST
            self.vx *= 0.98
            if abs(self.vy) < 0.7:
                self.vy = 0.0

        self.live -= 1
        stopped = (self.y + self.r >= H - 0.5 and abs(self.vx) < 0.15)
        if self.live <= 0 or stopped:
            canv.delete(self.id)
            self.live = 0
        else:
            self.set_coords()

    def hittest(self, ob):
        dx = self.x - ob.x
        dy = self.y - ob.y
        return dx * dx + dy * dy <= (self.r + ob.r) ** 2


class gun:
    """Класс gun описывает пушку."""

    def __init__(self, x=GX, y=GY):
        self.x, self.y = x, y
        self.f2_power = 15
        self.f2_on = 0
        self.an = -math.pi / 4
        self.id = canv.create_line(x, y, x + 25, y - 25, width=7)
        self.info = canv.create_text(130, 25, anchor='w', font='Arial 12', text='')

    def muzzle(self):
        """Координаты дула: ствол растёт вместе с силой выстрела."""
        length = max(self.f2_power, 20)
        return (self.x + length * math.cos(self.an),
                self.y + length * math.sin(self.an))

    def _draw(self):
        tx, ty = self.muzzle()
        canv.coords(self.id, self.x, self.y, tx, ty)
        canv.itemconfig(self.id, fill='orange' if self.f2_on else 'black')
        canv.itemconfig(self.info,
                        text=f'Сила: {self.f2_power:.0f}   '
                             f'Угол: {math.degrees(-self.an):.0f}°')

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event=None):
        """Выстрел: разлагаем скорость по выбранному углу."""
        global balls, bullet
        if not t1.live:
            return

        bullet += 1
        bx, by = self.muzzle()
        b = Ball(bx, by)
        b.r += 5
        b.vx = self.f2_power * math.cos(self.an)
        b.vy = self.f2_power * math.sin(self.an)
        balls.append(b)

        self.f2_on = 0
        self.f2_power = 15

    def targetting(self, event=0):
        """Прицеливание мышью: угол от пушки к курсору."""
        if event:
            an = math.atan2(event.y - self.y, event.x - self.x)
            if 0 < an < math.pi:
                an = -0.05 if event.x >= self.x else -math.pi + 0.05
            self.an = an
        self._draw()

    def power_up(self):
        if self.f2_on and self.f2_power < 60:
            self.f2_power += 0.5
        self._draw()

    def rotate(self, da):
        """Поворот ствола клавиатурой."""
        self.an = max(-math.pi + 0.05, min(-0.05, self.an + da))
        self._draw()

    def set_power(self, dp):
        """Изменение силы клавиатурой."""
        self.f2_power = max(5, min(60, self.f2_power + dp))
        self._draw()


class target:
    """Класс target описывает цель."""

    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0, fill='red')
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(20, 50)
        canv.coords(self.id, self.x - self.r, self.y - self.r,
                    self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill='red')

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

t1 = target()
g1 = gun()
screen1 = canv.create_text(W // 2, 100, text='', font='Arial 22')
balls = []


def new_game(event=None):
    global balls, bullet

    for b in balls:
        canv.delete(b.id)
    balls = []
    bullet = 0

    t1.new_target()
    t1.live = 1
    canv.itemconfig(screen1, text='')

    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    tick()


def tick():
    """Один кадр. root.after вместо while+sleep — мышь не «заикается»."""
    global balls

    g1.power_up()

    for b in balls:
        b.move()
        if t1.live and b.hittest(t1):
            t1.live = 0
            t1.hit()
            canv.itemconfig(screen1,
                            text=f'Цель уничтожена за {bullet} выстрел(а)!')
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')

    balls = [b for b in balls if b.live > 0]

    if not t1.live and not balls:
        root.after(1200, new_game)
    else:
        root.after(30, tick)


root.bind('<Left>',  lambda e: g1.rotate(-0.05))
root.bind('<Right>', lambda e: g1.rotate(0.05))
root.bind('<Up>',    lambda e: g1.set_power(2))
root.bind('<Down>',  lambda e: g1.set_power(-2))
root.bind('<space>', lambda e: g1.fire2_end())

new_game()
root.mainloop()