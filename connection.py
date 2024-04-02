#criar uma conexão com o servidor MQTT
# publicar mensagens em um tópico
# inscrever-se em um tópico
# receber mensagens de um tópico
# desconectar do servidor MQTT
# acionar o led via MQTT
# desligar o led via MQTT
import tkinter as tk
import paho.mqtt.client as mqtt

class SystemSupervisory:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Supervisório")
        
        self.label = tk.Label(self.root, text='Sistema Supervisório em Python para Instalações Industriais')
        self.label.pack()

        self.button = tk.Button(self.root, text="Acionar LED", command=self.publish_message)
        self.button.pack()
        
        self.button_exit = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.button_exit.pack()
        
        # Configurações MQTT
        self.mqtt_broker = "192.168.1.100"  # Substitua pelo endereço IP do seu ESP32
        self.mqtt_port = 1883
        self.mqtt_topic = "esp32/led"
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.mqtt_broker, self.mqtt_port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado ao broker MQTT com código de retorno: " + str(rc))
        client.subscribe(self.mqtt_topic)

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        if message == "ON":
            self.label.config(text="LED: Ligado")
        elif message == "OFF":
            self.label.config(text="LED: Desligado")

    def publish_message(self):
        message = "TOGGLE"
        self.client.publish(self.mqtt_topic, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemSupervisory(root)
    root.mainloop()

