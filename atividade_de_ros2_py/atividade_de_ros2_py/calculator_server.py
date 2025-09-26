#!/#!/usr/bin/env python3
#vamos fazer um servidor de calculadora simples usando ROS2 e Python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts           

class CalculatorServer(Node):
    def __init__(self):
        super().__init__('calculator_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Calculator Server está pronto para adicionar dois inteiros.')
        a = 0
        b = 0

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Recebido pedido: {request.a} + {request.b} = {response.sum}')
        return response
    
def main(args=None):
    rclpy.init(args=args)
    calculator_server = CalculatorServer()
    rclpy.spin(calculator_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()