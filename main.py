import tkinter as tk
from PIL import Image, ImageTk
import paho.mqtt.client as mqtt

class SystemSupervisory:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Supervisório")
        
        self.image = Image.open("the_flash_png_by_superflashofficial_de36frb-fullview.png")
        self.image = ImageTk.PhotoImage(self.image)
        
        self.label_image = tk.Label(self.root, image=self.image, width=900, height=300)
        self.label_image.pack()
        
        self.button_exit = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.button_exit.pack()
        
        self.button_start_click = tk.Button(self.root, text="Acionar LED", command=self.mqtt_publish)
        self.button_start_click.pack()
        
        # Configurações MQTT para se conectar ao ESP32
        self.mqtt_broker = "mqtt.eclipse.org"
        self.mqtt_port = 1883
        self.mqtt_topic = "esp32/led"
        
        # self.client = mqtt.Client()
        # self.client.on_connect = self.on_connect
        # self.client.connect(self.mqtt_broker, self.mqtt_port, 60)
        # self.client.loop_start()

    def on_connect(self, client, userdate, flags, rc):
        print("Conectado ao servidor MQTT")
        self.client.subscribe(self.mqtt_topic)
        print("Inscrito no tópico {}".format(self.mqtt_topic))

    def mqtt_publish(self):
        message = "TOGGLE"
        self.client.publish(self.mqtt_topic, message)
        
    def button_click(self):
        print("Botão clicado")
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemSupervisory(root)
    root.mainloop()
