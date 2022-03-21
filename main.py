from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
from fact_data import facts

import random


def choose_random_color():
    return random.choice(['Red', 'Pink', 'Purple', 'DeepPurple',
                          'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal',
                         'Green', 'LightGreen', 'Lime', 'Yellow',
                          'Amber', 'Orange', 'DeepOrange', 'Brown',
                          'Gray', 'BlueGray'])


class Main(MDBoxLayout):
    def __init__(self):
        super().__init__()

        # variable for identifiying index of current fact displayed
        self.current_index = 0

        self.fact_list = facts

        random.shuffle(self.fact_list)
        self.fact_label = self.ids.fact_here
        self.display_text()

    def next(self):
        # increment the current index by one,
        # if it not greater than the number of facts
        if self.current_index < len(self.fact_list)-1:
            self.current_index += 1
            self.display_text()

    def prev(self):
        # decrement the current index by one,
        # if it not greater than the number of facts

        if self.current_index != -len(self.fact_list):
            self.current_index -= 1
            self.display_text()

    def display_text(self):
        # Change the fact label to the fact in the current index
        self.fact_label.text = self.fact_list[self.current_index]

    # EXTRAS

    def open_youtube_channel(self):
        import webbrowser
        webbrowser.open(
            "https://www.youtube.com/channel/UC78UNf1yP6JbwtMXJwpdO6Q/")

    def open_twitter_account(self):
        import webbrowser
        webbrowser.open("https://www.twitter.com/abdulmuminYqn")

    def copy(self):
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(self.fact_list[self.current_index])


class DykApp(MDApp):
    app_mode = None

    def toggle(self):
        # toggle light or dark mode;
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'

        else:
            self.theme_cls.theme_style = 'Light'
        self.save_mode(self.theme_cls.theme_style)

    def save_mode(self, text):
        with open('mode.txt', 'w') as w:
            w.write(text)

    def on_start(self):
        self.theme_cls.primary_palette = 'Gray'
        try:
            mode_file = open('mode.txt').readline().strip()
            self.theme_cls.theme_style = mode_file
            mode_file.close()
        except:
            pass

    def build(self):
        LabelBase.register("quatum", "Quantum Profit.ttf")
        return Main()


app = DykApp()
app.run()
