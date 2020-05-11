from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'log_enable', 1)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1079')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import os
import subprocess
from kivy.clock import Clock
import time
import threading
import atexit

class Device:

    def __init__(self, ip, ui_component) -> None:
        super().__init__()
        self.ip = ip
        self.color = (1, .5, .2, 1)
        self.ui_component = ui_component

    def check(self):
            ping = "ping -l 8 " + self.ip
            result = subprocess.getoutput(ping)
            if ("(100% loss)," in result) or ("Destination host unreachable." in result):
               	self.color = (1, 0, 0, 1)
                self.ui_component.color = self.color
            else:
                self.color = (0, 1, 0, 1)
                self.ui_component.color = self.color
            

class Property:

    def __init__(self, mask_24, router_ui, dvr_ui, gate_ui) -> None:
        super().__init__()
        self.router = Device(mask_24[:-1] + '1', router_ui)
        self.dvr = Device(mask_24[:-1] + '101', dvr_ui)
        self.gate = Device(mask_24[:-1] + '103', gate_ui)

    def check(self):
	    while True:
	        self.router.check()
	        self.dvr.check()
	        self.gate.check()


class Dashboard(Screen):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.properties = [
            Property('10.100.1.0', self.router001, self.dvr001, self.gate001),
            Property('10.100.2.0', self.router002, self.dvr002, self.gate002),
            Property('10.100.3.0', self.router003, self.dvr003, self.gate003),
            Property('10.100.4.0', self.router004, self.dvr004, self.gate004),
            Property('10.100.5.0', self.router005, self.dvr005, self.gate005),
            Property('10.100.6.0', self.router006, self.dvr006, self.gate006),
            Property('10.100.7.0', self.router007, self.dvr007, self.gate007),
            Property('10.100.8.0', self.router008, self.dvr008, self.gate008),
            Property('10.100.9.0', self.router009, self.dvr009, self.gate009),
            Property('10.100.10.0', self.router010, self.dvr010, self.gate010),
            Property('10.100.11.0', self.router011, self.dvr011, self.gate011),
            Property('10.100.12.0', self.router012, self.dvr012, self.gate012),
            Property('10.100.13.0', self.router013, self.dvr013, self.gate013),
            Property('10.100.14.0', self.router014, self.dvr014, self.gate014),
            Property('10.100.15.0', self.router015, self.dvr015, self.gate015),
            Property('10.100.16.0', self.router016, self.dvr016, self.gate016),
            Property('10.100.17.0', self.router017, self.dvr017, self.gate017),
            Property('192.168.1.0', self.router018, self.dvr018, self.gate018),
            Property('10.100.20.0', self.router020, self.dvr020, self.gate020),
            Property('10.100.21.0', self.router021, self.dvr021, self.gate021),
            Property('10.100.22.0', self.router022, self.dvr022, self.gate022),
            Property('10.100.23.0', self.router023, self.dvr023, self.gate023),
            Property('10.100.24.0', self.router024, self.dvr024, self.gate024),
            Property('10.100.25.0', self.router025, self.dvr025, self.gate025),
            Property('10.100.26.0', self.router026, self.dvr026, self.gate026),
            Property('10.100.27.0', self.router027, self.dvr027, self.gate027),
            Property('10.100.28.0', self.router028, self.dvr028, self.gate028),
            Property('10.100.29.0', self.router029, self.dvr029, self.gate029),
            Property('10.100.30.0', self.router030, self.dvr030, self.gate030),
            Property('10.100.31.0', self.router031, self.dvr031, self.gate031),
            Property('10.100.32.0', self.router032, self.dvr032, self.gate032),
            Property('10.100.33.0', self.router033, self.dvr033, self.gate033),
            Property('10.100.34.0', self.router034, self.dvr034, self.gate034),
            Property('10.100.35.0', self.router035, self.dvr035, self.gate035),
            Property('10.100.36.0', self.router036, self.dvr036, self.gate036),
            Property('10.100.37.0', self.router037, self.dvr037, self.gate037),
            Property('10.100.38.0', self.router038, self.dvr038, self.gate038),
            Property('10.100.39.0', self.router039, self.dvr039, self.gate039),
            Property('10.100.40.0', self.router040, self.dvr040, self.gate040),
            Property('10.100.44.0', self.router044, self.dvr044, self.gate044),
            Property('10.100.45.0', self.router045, self.dvr045, self.gate045),
            Property('10.100.46.0', self.router046, self.dvr046, self.gate046),
            Property('10.100.47.0', self.router047, self.dvr047, self.gate047),
            Property('10.100.59.0', self.router059, self.dvr059, self.gate059),
            Property('10.100.60.0', self.router060, self.dvr060, self.gate060),
            Property('10.100.61.0', self.router061, self.dvr061, self.gate061),
            Property('10.100.62.0', self.router062, self.dvr062, self.gate062),
            Property('10.100.70.0', self.router070, self.dvr070, self.gate070),
            Property('10.100.71.0', self.router071, self.dvr071, self.gate071),
            Property('10.101.71.0', self.router171, self.dvr171, self.gate171),
            Property('10.101.72.0', self.router172, self.dvr172, self.gate172),
            Property('10.101.73.0', self.router173, self.dvr173, self.gate173),
            Property('10.101.74.0', self.router174, self.dvr174, self.gate174),
            Property('10.101.75.0', self.router175, self.dvr175, self.gate175),
            Property('10.101.77.0', self.router177, self.dvr177, self.gate177),
            Property('10.101.78.0', self.router178, self.dvr178, self.gate178),
            Property('10.102.1.0', self.router201, self.dvr201, self.gate201),
            Property('10.102.2.0', self.router202, self.dvr202, self.gate202),
            Property('10.102.3.0', self.router203, self.dvr203, self.gate203),
            Property('10.102.4.0', self.router204, self.dvr204, self.gate204),
            Property('10.103.1.0', self.router301, self.dvr301, self.gate301),
            Property('10.103.2.0', self.router302, self.dvr302, self.gate302),
            Property('10.103.3.0', self.router303, self.dvr303, self.gate303),
            Property('10.103.4.0', self.router304, self.dvr304, self.gate304),
            Property('10.103.5.0', self.router305, self.dvr305, self.gate305),
            Property('10.103.6.0', self.router306, self.dvr306, self.gate306),
            Property('10.103.7.0', self.router307, self.dvr307, self.gate307),
            Property('10.103.8.0', self.router308, self.dvr308, self.gate308),
            Property('10.103.9.0', self.router309, self.dvr309, self.gate309),
            Property('10.103.10.0', self.router310, self.dvr310, self.gate310),
            Property('10.103.11.0', self.router311, self.dvr311, self.gate311),
            Property('10.103.12.0', self.router312, self.dvr312, self.gate312),
            Property('10.103.13.0', self.router313, self.dvr313, self.gate313),
            Property('10.103.14.0', self.router314, self.dvr314, self.gate314),
            Property('10.103.15.0', self.router315, self.dvr315, self.gate315),
            Property('10.103.16.0', self.router316, self.dvr316, self.gate316),
            Property('10.103.17.0', self.router317, self.dvr317, self.gate317),
            Property('10.103.52.0', self.router352, self.dvr352, self.gate352),
            Property('10.103.54.0', self.router354, self.dvr354, self.gate354),
            Property('10.103.55.0', self.router355, self.dvr355, self.gate355),
            Property('10.104.2.0', self.router402, self.dvr402, self.gate402),
            Property('10.104.3.0', self.router403, self.dvr403, self.gate403),
            Property('10.104.25.0', self.router425, self.dvr425, self.gate425),
            Property('10.104.28.0', self.router428, self.dvr428, self.gate428),
            Property('10.104.29.0', self.router429, self.dvr429, self.gate429),
            Property('10.104.32.0', self.router432, self.dvr432, self.gate432),
            Property('10.104.33.0', self.router433, self.dvr433, self.gate433),
            Property('10.104.34.0', self.router434, self.dvr434, self.gate434),
            Property('10.104.35.0', self.router435, self.dvr435, self.gate435),
            Property('10.104.36.0', self.router436, self.dvr436, self.gate436),
            Property('10.104.37.0', self.router437, self.dvr437, self.gate437),
            Property('10.104.38.0', self.router438, self.dvr438, self.gate438),
            Property('10.104.39.0', self.router439, self.dvr439, self.gate439),
            Property('10.104.40.0', self.router440, self.dvr440, self.gate440),
            Property('10.104.43.0', self.router443, self.dvr443, self.gate443),
            Property('10.104.44.0', self.router444, self.dvr444, self.gate444),
            Property('10.104.45.0', self.router445, self.dvr445, self.gate445),
            Property('10.104.50.0', self.router450, self.dvr450, self.gate450),
            Property('10.104.51.0', self.router451, self.dvr451, self.gate451),
            Property('10.104.52.0', self.router452, self.dvr452, self.gate452),
            Property('10.104.53.0', self.router453, self.dvr453, self.gate453),
            Property('10.104.54.0', self.router454, self.dvr454, self.gate454),
            Property('10.104.55.0', self.router455, self.dvr455, self.gate455),
            Property('10.104.56.0', self.router456, self.dvr456, self.gate456),
            Property('10.105.1.0', self.router501, self.dvr501, self.gate501),
            Property('10.105.2.0', self.router502, self.dvr502, self.gate502),
            Property('10.105.3.0', self.router503, self.dvr503, self.gate503),
            Property('10.105.4.0', self.router504, self.dvr504, self.gate504),
            Property('10.105.5.0', self.router505, self.dvr505, self.gate505),
            Property('10.105.6.0', self.router506, self.dvr506, self.gate506),
            Property('10.105.7.0', self.router507, self.dvr507, self.gate507),

        ]

        self.id_labels = [self.id001, self.id002, self.id003, self.id004,
        	self.id005, self.id006, self.id007, self.id008, self.id009,
            self.id010, self.id011, self.id012, self.id013, self.id014,
            self.id015, self.id016, self.id017, self.id018, self.id020,
            self.id021, self.id022, self.id023, self.id024, self.id025, self.id026,
            self.id027, self.id028, self.id029, self.id030, self.id031,
            self.id032, self.id033, self.id034, self.id035, self.id036,
            self.id037, self.id038, self.id039, self.id040, self.id044,
            self.id045, self.id046, self.id047, self.id059, self.id060,
            self.id061, self.id062, self.id070, self.id071, self.id171,
            self.id172, self.id173, self.id174, self.id175, self.id177,
            self.id178, self.id201, self.id202, self.id203, self.id204,
            self.id301, self.id302, self.id303, self.id304, self.id305,
            self.id306, self.id307, self.id308, self.id309, self.id310,
            self.id311, self.id312, self.id313, self.id314, self.id315,
            self.id316, self.id317, self.id352, self.id354, self.id355,
            self.id402, self.id403, self.id425, self.id428, self.id429,
            self.id432, self.id433, self.id434, self.id435, self.id436,
            self.id437, self.id438, self.id439, self.id440, self.id443,
            self.id444, self.id445, self.id450, self.id451, self.id452,
            self.id453, self.id454, self.id455, self.id456, self.id501,
            self.id502, self.id503, self.id504, self.id505, self.id506,
            self.id507,
        ]

        self.router_labels = [self.router001, self.router002, self.router003, self.router004,
            self.router005, self.router006, self.router007, self.router008, self.router009,
            self.router010, self.router011, self.router012, self.router013, self.router014,
            self.router015, self.router016, self.router017, self.router018, self.router020,
            self.router021, self.router022, self.router023, self.router024, self.router025, self.router026,
            self.router027, self.router028, self.router029, self.router030, self.router031,
            self.router032, self.router033, self.router034, self.router035, self.router036,
            self.router037, self.router038, self.router039, self.router040, self.router044,
            self.router045, self.router046, self.router047, self.router059, self.router060,
            self.router061, self.router062, self.router070, self.router071, self.router171,
            self.router172, self.router173, self.router174, self.router175, self.router177,
            self.router178, self.router201, self.router202, self.router203, self.router204,
            self.router301, self.router302, self.router303, self.router304, self.router305,
            self.router306, self.router307, self.router308, self.router309, self.router310,
            self.router311, self.router312, self.router313, self.router314, self.router315,
            self.router316, self.router317, self.router352, self.router354, self.router355,
            self.router402, self.router403, self.router425, self.router428, self.router429,
            self.router432, self.router433, self.router434, self.router435, self.router436,
            self.router437, self.router438, self.router439, self.router440, self.router443,
            self.router444, self.router445, self.router450, self.router451, self.router452,
            self.router453, self.router454, self.router455, self.router456, self.router501,
            self.router502, self.router503, self.router504, self.router505, self.router506,
            self.router507,
        ]

        self.dvr_labels = [self.dvr001, self.dvr002, self.dvr003, self.dvr004,
        	self.dvr005, self.dvr006, self.dvr007, self.dvr008, self.dvr009,
            self.dvr010, self.dvr011, self.dvr012, self.dvr013, self.dvr014,
            self.dvr015, self.dvr016, self.dvr017, self.dvr018, self.dvr020,
            self.dvr021, self.dvr022, self.dvr023, self.dvr024, self.dvr025, self.dvr026,
            self.dvr027, self.dvr028, self.dvr029, self.dvr030, self.dvr031,
            self.dvr032, self.dvr033, self.dvr034, self.dvr035, self.dvr036,
            self.dvr037, self.dvr038, self.dvr039, self.dvr040, self.dvr044,
            self.dvr045, self.dvr046, self.dvr047, self.dvr059, self.dvr060,
            self.dvr061, self.dvr062, self.dvr070, self.dvr071, self.dvr171,
            self.dvr172, self.dvr173, self.dvr174, self.dvr175, self.dvr177,
            self.dvr178, self.dvr201, self.dvr202, self.dvr203, self.dvr204,
            self.dvr301, self.dvr302, self.dvr303, self.dvr304, self.dvr305,
            self.dvr306, self.dvr307, self.dvr308, self.dvr309, self.dvr310,
            self.dvr311, self.dvr312, self.dvr313, self.dvr314, self.dvr315,
            self.dvr316, self.dvr317, self.dvr352, self.dvr354, self.dvr355,
            self.dvr402, self.dvr403, self.dvr425, self.dvr428, self.dvr429,
            self.dvr432, self.dvr433, self.dvr434, self.dvr435, self.dvr436,
            self.dvr437, self.dvr438, self.dvr439, self.dvr440, self.dvr443,
            self.dvr444, self.dvr445, self.dvr450, self.dvr451, self.dvr452,
            self.dvr453, self.dvr454, self.dvr455, self.dvr456, self.dvr501,
            self.dvr502, self.dvr503, self.dvr504, self.dvr505, self.dvr506,
            self.dvr507,
        ]

        self.gate_labels = [self.gate001, self.gate002, self.gate003, self.gate004,
        	self.gate005, self.gate006, self.gate007, self.gate008, self.gate009,
            self.gate010, self.gate011, self.gate012, self.gate013, self.gate014,
            self.gate015, self.gate016, self.gate017, self.gate018, self.gate020,
            self.gate021, self.gate022, self.gate023, self.gate024, self.gate025, self.gate026,
            self.gate027, self.gate028, self.gate029, self.gate030, self.gate031,
            self.gate032, self.gate033, self.gate034, self.gate035, self.gate036,
            self.gate037, self.gate038, self.gate039, self.gate040, self.gate044,
            self.gate045, self.gate046, self.gate047, self.gate059, self.gate060,
            self.gate061, self.gate062, self.gate070, self.gate071, self.gate171,
            self.gate172, self.gate173, self.gate174, self.gate175, self.gate177,
            self.gate178, self.gate201, self.gate202, self.gate203, self.gate204,
            self.gate301, self.gate302, self.gate303, self.gate304, self.gate305,
            self.gate306, self.gate307, self.gate308, self.gate309, self.gate310,
            self.gate311, self.gate312, self.gate313, self.gate314, self.gate315,
            self.gate316, self.gate317, self.gate352, self.gate354, self.gate355,
            self.gate402, self.gate403, self.gate425, self.gate428, self.gate429,
            self.gate432, self.gate433, self.gate434, self.gate435, self.gate436,
            self.gate437, self.gate438, self.gate439, self.gate440, self.gate443,
            self.gate444, self.gate445, self.gate450, self.gate451, self.gate452,
            self.gate453, self.gate454, self.gate455, self.gate456, self.gate501,
            self.gate502, self.gate503, self.gate504, self.gate505, self.gate506,
            self.gate507,
        ]
    
        x = -0.235
        y = 0.9
        for i in self.id_labels:
        	if x == -0.235 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == -0.235 and y < -0.05:
        		x = 0.1
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.1 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.1 and y < -0.05:
        		x = 0.432
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.432 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	else:
        		print ('x is '+str(x))
        		print ('y is ' +str(y))
        	y = y - 0.025

        x = -0.185
        y = 0.9
        for i in self.router_labels:
        	if x == -0.185 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == -0.185 and y < -0.05:
        		x = 0.14
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.14 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.14 and y < -0.05:
        		x = 0.47
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.47 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	else:
        		print ('x is '+str(x))
        		print ('y is ' +str(y))
        	y = y - 0.025
        x = -0.08
        y = 0.9
        for i in self.dvr_labels:
        	if x == -0.08 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == -0.08 and y < -0.05:
        		x = 0.24
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.24 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.24 and y < -0.05:
        		x = 0.58
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.58 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	else:
        		print ('x is '+str(x))
        		print ('y is ' +str(y))
        	y = y - 0.025
        x = 0.045
        y = 0.9
        for i in self.gate_labels:
        	if x == 0.045 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.045 and y < -0.05:
        		x = 0.38
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.38 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.38 and y < -0.05:
        		x = 0.71
        		y = 0.9
        		i.pos_hint = {'x': x, 'y': y}
        	elif x == 0.71 and y > -0.05:
        		i.pos_hint = {'x': x, 'y': y}
        	else:
        		print ('x is '+str(x))
        		print ('y is ' +str(y))
        	y = y - 0.025


    def start_ping(self):
        for property in self.properties:
            threading.Timer(1, property.check).start()



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("GateDashboard.kv")
sm = WindowManager()

screens = [Dashboard(name="dashboard")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "dashboard"

class Gate_DashboardApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
    Gate_DashboardApp().run()