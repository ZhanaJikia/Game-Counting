# Python Using Tkinter

© 2017 by Revel Carlberg West. All rights reserved.

Tkinter is way for kids
to use GUIs. That creates a
basic window like this:

![image](https://user-images.githubusercontent.com/29359616/29250831-87a1bbb8-8017-11e7-8b51-b686a6ac75e8.png)

with just the code:

```python

import tkinter

window = tkinter.Tk()

```

and than you can add stuff to it
like this:

![image](https://user-images.githubusercontent.com/29359616/29250841-a7f4c25c-8017-11e7-9cd2-2444415ee0c8.png)

but of course the button doesn't
do anything because we
didn't tell it to do something

```python

import tkinter

window = tkinter.Tk()
                  #defines a button. "window" means
                  #put the button the window, and
                  #"text=" means what the button
                  #should say
button = tkinter.Button(window, text='Press Me')
button.pack()#tells the button to go on the window

```

so I modified it so it would do
something when you click it, and that something was
print "hello world"

![image](https://user-images.githubusercontent.com/29359616/29250814-314ae91a-8017-11e7-9faa-88ef4b5d509f.png)

and this is the code i used to
make the button print hello world

```python

import tkinter

def do_something():
    print('hello world')

window = tkinter.Tk()

button = tkinter.Button(window, text='Press Me', command=do_something)
button.pack()

```


## Useful links



1. [Python GUI with Tkinter - 1 - Introduction](https://www.youtube.com/watch?v=RJB1Ek2Ko_Y)

- [Python GUI with Tkinter - 2 - Organizing your Layout](https://www.youtube.com/watch?v=RTM9tiV_HoY)

- [Python GUI with Tkinter - 3 - Fitting Widgets in your Layout](https://www.youtube.com/watch?v=Ko4EPJ8DDjg&t=8s)

- [Python GUI with Tkinter - 4 - Grid Layout](https://www.youtube.com/watch?v=-nmzq3xiZ6I)

- [Python GUI with Tkinter - 5 - More on the Grid Layout](https://www.youtube.com/watch?v=wNBqM28MMjs)

- [Python GUI with Tkinter - 6 - Binding Functions to Layouts](https://www.youtube.com/watch?v=qWnE-yp6wzU)

- [Python GUI with Tkinter - 7 - Mouse Click Events](https://www.youtube.com/watch?v=XkCbinbgbdw)
