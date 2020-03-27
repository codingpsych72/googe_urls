import kivy
import kivy.app
import kivy.uix.textinput,kivy.uix.boxlayout,kivy.uix.label,kivy.uix.button
import os
from googlesearch import search

# Now access the texture of the label and use it wherever and
# however you may please.


class ggly(kivy.app.App):
    def build(self):
        self.boxy=kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.textinput1=kivy.uix.textinput.TextInput(text="enter the key word to search")
        self.butty=kivy.uix.button.Button(text="start search")
        self.butty.bind(on_press=self.goole_search)
        self.boxy.add_widget(self.textinput1)
        self.boxy.add_widget(self.butty)
        return self.boxy
    def goole_search(self,name):
        name=self.textinput1.text

        head = []
        for i in search(query=name, lang='en', tld='com', num=10, start=0, stop=10, pause=2.0):
            head.append(i)
        for i in head:
            with open("log.txt", 'a+') as n:
                n.write(i + '\n')
        os.system("gedit log.txt ")


if __name__=="__main__":
    a=ggly()
    a.run()
