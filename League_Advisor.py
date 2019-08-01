#from numpy import loadtxt
#from keras.models import Sequential
import tkinter as tk






#sets up the gui
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()



#creates the widgets
    def create_widgets(self):
        #Lane Buttons
        self.Lane_Title= tk.Label(self, text = "Lane:", fg = "#0099cc")
        self.Lane_Title.pack(padx = 10, pady = 10, side = "left", anchor = "nw")
        #variables
        self.answered_lane = -1
        self.answered_enemy = -1
        self.enemy_or_type_button = -1
        self.example_choices = [
        [0,0,3],
        [1,2,0],
        [2,2,2],
        [3,3,4],
        [4,1,3],
        [0,1,0]
        ]
        self.type = ""
        self.lane = 0
        self.enemy = 0
        self.mid = tk.Button(self)
        self.mid["text"] = "Mid"
        self.mid["bg"] = "#3399ff"
        self.mid.pack(padx=5, pady=10,side="left")
        self.mid["command"]= self.mid_lane_picker


        #Top Lane Button setup
        self.top = tk.Button(self, text ="Top", bg = "#3399ff", command = self.top_lane_picker)
        self.top.pack(padx=10, pady=10,side="left")
        #Jungle Lane Button setup
        self.jg = tk.Button(self, text = "Jungle", bg = "#3399ff", command = self.jungle_lane_picker)
        self.jg.pack(padx=10, pady=10,side= "left")
        #Bot lane Button setup
        self.bottom = tk.Button(self, text = "ADC", bg = "#3399ff", command = self.bottom_lane_picker)
        self.bottom.pack(padx=10, pady=10, side = "left")
        #Support Lane Button setup
        self.sup = tk.Button(self, text = "Support", bg ="#3399ff", command = self.support_lane_picker)
        self.sup.pack(padx=10, pady=10, side = "left")

        self.Enemy_Title= tk.Label(self, text = "Lane:", fg = "#0099cc")
        self.Enemy_Title.pack(padx = 10, pady = 10, side = "left", anchor = "nw")
        #Bruser Enemy Button Setup
        self.brusier = tk.Button(self, text = "Bruser", bg = "#33ccff", command = self.bruser_enemey_picker)
        self.brusier.pack(padx =10, pady = 5, side = "left")
        #Tank Enemy Button Setup
        self.tank = tk.Button(self, text = "Tank", bg = "#33ccff", command = self.tank_enemy_picker)
        self.tank.pack(padx =10, pady = 5, side = "left")
        #Ranger Enemy Button Setup
        self.ranger = tk.Button(self, text = "Ranger", bg = "#33ccff", command = self.ranger_enemy_picker)
        self.ranger.pack(padx =10, pady = 5, side = "left")
        #Mage Enemy Button Setup
        self.Mage = tk.Button(self, text = "Mage", bg = "#33ccff", command = self.mage_enemy_picker)
        self.Mage.pack(padx =10, pady = 5, side = "left")
        #Assasin Enemey Button Setup
        self.Assasin = tk.Button(self, text = "Assasin", bg = "#33ccff", command = self.assasin_enemy_picker)
        self.Assasin.pack(padx =10, pady = 5, side = "left")




        #Reset Button!!!! to Fix all our mistakes....
        self.reset = tk.Button(self, text = "Reset", command = self.reset_attributes)
        self.reset.pack(padx = 5, pady = 20, side= "bottom")
        #Tells you it's guess of who you picked
        self.guess = tk.Text(self, height= "2", width = "20")
        self.guess.pack(padx = 5, pady = 10, side="bottom");
        self.guess.insert(tk.END,self.type)



        #<---------Visual Effects--------------->
    def top_lane_picker(self):
        if self.answered_lane == -1:
            self.enemy_or_type_button = 0
            self.lane = 0
            self.mid["bg"] = "#000099"
            self.jg["bg"] = "#000099"
            self.bottom["bg"] = "#000099"
            self.sup["bg"] = "#000099"
            self.button_action()


    def mid_lane_picker(self):
        if self.answered_lane == -1:
            self.enemy_or_type_button=0
            self.lane = 1
            self.top["bg"] = "#000099"
            self.jg["bg"] = "#000099"
            self.bottom["bg"] = "#000099"
            self.sup["bg"] = "#000099"
            self.button_action()


    def jungle_lane_picker(self):
        if self.answered_lane ==-1:
            self.enemy_or_type_button=0
            self.lane = 2
            self.mid["bg"] = "#000099"
            self.top["bg"] = "#000099"
            self.bottom["bg"] = "#000099"
            self.sup["bg"] = "#000099"
            self.button_action()


    def bottom_lane_picker(self):
        if self.answered_lane == -1:
            self.enemy_or_type_button=0
            self.lane=3
            self.mid["bg"] = "#000099"
            self.jg["bg"] = "#000099"
            self.top["bg"] = "#000099"
            self.sup["bg"] = "#000099"
            self.button_action()


    def support_lane_picker(self):
        if self.answered_lane == -1:
                self.enemy_or_type_button=0
                self.lane=4
                self.mid["bg"] = "#000099"
                self.jg["bg"] = "#000099"
                self.bottom["bg"] = "#000099"
                self.top["bg"] = "#000099"
                self.button_action()

    def bruser_enemey_picker(self):
        if self.answered_enemy == -1:
            self.enemy_or_type_button=1
            self.enemy=0
            self.tank["bg"] = "#0099cc"
            self.Assasin["bg"] = "#0099cc"
            self.ranger["bg"] = "#0099cc"
            self.Mage["bg"] = "#0099cc"
            self.button_action()

    def tank_enemy_picker(self):
        if self.answered_enemy == -1:
            self.enemy_or_type_button=1
            self.enemy=1
            self.brusier["bg"] = "#0099cc"
            self.Assasin["bg"] = "#0099cc"
            self.ranger["bg"] = "#0099cc"
            self.Mage["bg"] = "#0099cc"
            self.button_action()

    def assasin_enemy_picker(self):
        if self.answered_enemy == -1:
            self.enemy_or_type_button=1
            self.enemy=2
            self.tank["bg"] = "#0099cc"
            self.brusier["bg"] = "#0099cc"
            self.ranger["bg"] = "#0099cc"
            self.Mage["bg"] = "#0099cc"
            self.button_action()

    def mage_enemy_picker(self):
        if self.answered_enemy == -1:
            self.enemy_or_type_button=1
            self.enemy=3
            self.tank["bg"] = "#0099cc"
            self.Assasin["bg"] = "#0099cc"
            self.ranger["bg"] = "#0099cc"
            self.brusier["bg"] = "#0099cc"
            self.button_action()

    def ranger_enemy_picker(self):
        if self.answered_enemy == -1:
            self.enemy_or_type_button=1
            self.enemy=4
            self.tank["bg"] = "#0099cc"
            self.Assasin["bg"] = "#0099cc"
            self.brusier["bg"] = "#0099cc"
            self.Mage["bg"] = "#0099cc"
            self.button_action()

    def reset_attributes(self):
        self.answered_lane=-1
        self.answered_enemy = -1
        self.enemy_or_type_button = -1;
        self.guess.delete("1.0",tk.END)
        self.mid["bg"] = "#3399ff"
        self.jg["bg"] = "#3399ff"
        self.bottom["bg"] = "#3399ff"
        self.top["bg"] = "#3399ff"
        self.sup["bg"] = "#3399ff"
        self.brusier["bg"] = "#33ccff"
        self.Assasin["bg"] = "#33ccff"
        self.tank["bg"] = "#33ccff"
        self.ranger["bg"] = "#33ccff"
        self.Mage["bg"] = "#33ccff"
        self.button_action()
        #What to do technically when button is pressed
    def button_action(self):
        if self.answered_lane == -1 and self.enemy_or_type_button == 0:
            self.answered_lane = 1
        if self.answered_enemy == -1 and self.enemy_or_type_button ==1:
            self.answered_enemy = 1
        if(self.answered_lane == 1 and self.answered_enemy == 1):
            #self.build_tree(example_choices)
            self.give_result()





    #def build_tree(self,data_set):
        #info, question =

    #self.tree = self.build_tree(self.example_choices)

    def rules(self,lane,enemy):
        self.result = 0
        if lane == 0:
            if enemy == 0:
                self.result = 4
            elif enemy == 1:
                self.result = 3
        if lane == 1:
            if enemy == 0:
                self.result = 3
            elif enemy == 3:
                self.result = 2
            elif enemy == 2:
                self.result = 0
        if lane == 2:
            if enemy == 2:
                self.result = 0
            elif enemy == 0:
                self.result = 4
            elif enemy == 3:
                self.result = 2
        if lane == 3:
            if enemy == 4:
                self.result = 4
            elif enemy == 2:
                self.result = 0
            elif enemy == 3:
                self.result = 4
        if lane == 4:
            if enemy == 0:
                self.result =3
            elif enemy == 1:
                self.result = 1
            elif enemy == 3:
                self.result = 1
    def translate_result(self, result):
        if result == 0:
            return "Bruser"
        elif result == 1:
            return "Tank"
        elif result ==2:
            return "Assasin"
        elif result ==3:
            return "Mage"
        elif result == 4:
            return "Range"

    def give_result(self):

        self.rules(self.lane,self.enemy)
        self.word_result = self.translate_result(self.result)
        self.type = "Pick a " + self.word_result
        print(self.type)
        self.guess.insert(tk.END,self.type)


























root = tk.Tk()
root.title("Princeton_Learning_Machine")
app = Application(master=root)
app.mainloop()
