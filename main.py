from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from fact_data import facts


class Main(MDBoxLayout):
    def __init__(self):
        super().__init__()

        # variable for identifiying index of current fact displayed
        self.current_index = 0
        self.fact_list = facts

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
        webbrowser.open("https://www.twitter.com/abdulmu45677579")


class DykApp(MDApp):
    app_mode = None

    def toggle(self):
        # toggle light or dark mode;
        if self.app_mode:
            self.theme_cls.theme_style = 'Light'
            self.app_mode = False
            self.save_mode('Light')
        else:
            self.theme_cls.theme_style = 'Dark'
            self.app_mode = True
            self.theme_cls.primary_palette = 'Amber'

            self.save_mode('Dark')

    def save_mode(self, text):
        with open('mode.txt', 'w') as w:
            w.write(text)

    def on_start(self):
        try:
            mode_file = open('mode.txt').readline().strip()
            self.theme_cls.theme_style = mode_file
            mode_file.close()
        except:
            pass

    def build(self):
        return Main()


app = DykApp()
app.run()
