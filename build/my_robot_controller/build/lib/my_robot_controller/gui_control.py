import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import sys

class GUIController(Node):
    def __init__(self):
        super().__init__('gui_control_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Control del Robot")
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((240, 240, 240))

            # Dibujar líneas divisorias
            pygame.draw.line(self.screen, (0, 0, 0), (300, 0), (300, 600), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (0, 300), (600, 300), 2)

            # Dibujar círculo central para "stop"
            pygame.draw.circle(self.screen, (255, 100, 100), (300, 300), 40)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    twist = Twist()

                    dx = x - 300
                    dy = y - 300
                    dist = (dx**2 + dy**2)**0.5

                    if dist < 40:
                        # Parar (clic en el centro)
                        twist.linear.x = 0.0
                        twist.angular.z = 0.0
                        self.get_logger().info("Stop")

                    elif y < 200:
                        twist.linear.x = 0.3
                        twist.angular.z = 0.0
                        self.get_logger().info("Adelante")

                    elif y > 400:
                        twist.linear.x = -0.3
                        twist.angular.z = 0.0
                        self.get_logger().info("Atrás")

                    elif x < 200:
                        twist.linear.x = 0.0
                        twist.angular.z = 1.0
                        self.get_logger().info("Girar izquierda")

                    elif x > 400:
                        twist.linear.x = 0.0
                        twist.angular.z = -1.0
                        self.get_logger().info("Girar derecha")

                    self.publisher.publish(twist)

        pygame.quit()


def main(args=None):
    rclpy.init(args=args)
    node = GUIController()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

