"""
An all in one skin generator
    - generate skin_racks from trained tensorflow model
    - cut racks to single skins and generate skin thumbnail
    - loop through all thumbnail and select yes or no (multiple passage)
    - output skin pack

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.config import Config
from kivy.properties import ObjectProperty, StringProperty

import os

Config.set('graphics', 'resizable', 0)

class AllInOneScreen(Screen):
    def generate(self):
        command = "python3 DCGAN-tensorflow/main.py --dataset=Rainbow --out_name='model' --input_height=64 --output_height=64 --input_fname_pattern=*.png --batch_size=30 --train=false --out_dir=./ --crop=false --visualize=true"
        os.system(command)
        os.system('python3 process.py')


class SelectionScreen(Screen):
    skins_thumb = ObjectProperty()

    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        self.i = 0
        self.img_src = 'Output/skins_thumb/' + str(self.i) + '.png'

    def good(self):
        with open('Output/good_ones/good.txt', 'a+') as file:
            file.write(str(self.i) + '\n')
            file.close()
        os.system('mv ' + self.img_src + ' Output/good_ones/thumbs/' + str(self.i) + '.png')
        os.system('mv Output/skins/' + str(self.i) + '.png Output/good_ones/skins/' + str(self.i) + '.png')
        self.next()

    def bad(self):
        os.system('rm -rf ' + self.img_src)
        os.system('rm -rf Output/skins/' + str(self.i) + '.png')
        self.next()

    def next(self):
        self.i += 1
        self.img_src = 'Output/skins_thumb/' + str(self.i) + '.png'
        self.skins_thumb.source = self.img_src


class MainScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Main(App):

    def build(self):
        self.title = 'xXx_MC_GEN_xXx'
        return


if __name__ == '__main__':
    Main().run()
