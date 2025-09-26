#!/#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class Assinante(Node):
    def __init__(self):
        super().__init__('assinante')
        self.get_logger().info('Nó "assinante" iniciado.')
        self.subscription = self.create_subscription(String,'topico', self.listener_callback, 10)
        self.subscription  # evitar aviso de variável não utilizada

    def listener_callback(self, msg):
        self.get_logger().info(f'Recebido: "{msg.data}"')
    
def main(args=None):
    rclpy.init(args=args)
    assinante = Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()

if __name__ == '__main__':
    main() 