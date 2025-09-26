#!/#!/usr/bin/env python3
#vamos fazer um cliente de calculadora simples usando ROS2 e Python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class CalculatorClient(Node):
    def __init__(self):
        super().__init__('calculator_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço não disponível, esperando...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
    
def main(args=None):
    rclpy.init(args=args)
    calculator_client = CalculatorClient()
    a = 5
    b = 3
    calculator_client.send_request(a, b)

    while rclpy.ok():
        rclpy.spin_once(calculator_client)
        if calculator_client.future.done():
            try:
                response = calculator_client.future.result()
            except Exception as e:
                calculator_client.get_logger().info(f'Serviço falhou: {e}')
            else:
                calculator_client.get_logger().info(f'Resultado: {a} + {b} = {response.sum}')
            break

    calculator_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()