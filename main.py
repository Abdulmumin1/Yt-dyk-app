from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from fact_data import facts

class Main(MDBoxLayout):
    def __init__(self):
        super().__init__()

        self.current_index = 0
        self.fact_list = facts

        self.fact_label = self.ids.fact_here
        self.display_text()
    
    def next(self):
        if self.current_index < len(self.fact_list)-1:
            self.current_index +=1 
            self.display_text()

    def prev(self):
        if self.current_index != -len(self.fact_list):
            self.current_index -= 1
            self.display_text()

    def display_text(self):
        self.fact_label.text  =self.fact_list[self.current_index]

class DykApp(MDApp):
    app_mode  = None

    def toggle(self):
        if self.app_mode:
            self.theme_cls.theme_style = 'Light'
            self.app_mode = False
            self.save_mode('Light')
        else:
            self.theme_cls.theme_style = 'Dark'
            self.app_mode = True
            self.save_mode('Dark')
    
    def save_mode(self, text):
        with open('mode.txt', 'w') as w:
            w.write(text)
    def build(self):
        try:
            self.theme_cls.theme_style = open('mode.txt').readline().strip()
        except:
            pass
        return Main()

app = DykApp()
app.run()