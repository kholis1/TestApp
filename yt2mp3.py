from pytube import YouTube
import os

import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter URL of youtube video: "))
        self.url = TextInput(multiline=False)
        self.inside.add_widget(self.url)

        self.add_widget(self.inside)

        self.submit = Button(text="Download", font_size=40)
        self.submit.bind(on_press=self.download)
        self.add_widget(self.submit)

    def download(self, instance):
        url = self.url.text
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        print("Enter the destination address (leave blank to save in current directory)")
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
