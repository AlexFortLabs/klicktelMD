from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty

#klicks: int

class MainApp(MDApp):

    #klicks = ObjectProperty(None)


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('myform.kv')

    def suchen(self):
        #self.klcks = self.klicks + 1
        #self.root.ids.my_label.text = str(self.klcks)
        self.root.ids.my_label.text = "Hast te ja geklicktest."

    def info(self):
        self.root.ids.my_label.text = "Hier wird ein\n Dialog entstehen"


MainApp().run()
