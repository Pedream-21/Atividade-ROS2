#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publicador(Node):
    def __init__(self):
        super().__init__('publicador')
        self.get_logger().info('Nó "publicador" iniciado.')
        self.publisher_ = self.create_publisher(String, 'topico', 10)
        timer_period = 1.0  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS 2! {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    publicador = Publicador()
    rclpy.spin(publicador)
    rclpy.shutdown()

if __name__ == '__main__':
    main()