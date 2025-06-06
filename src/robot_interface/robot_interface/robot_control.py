import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import tkinter as tk

class RobotControl(Node):
    def __init__(self):
        super().__init__('robot_control')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info("Robot control node started")
        self.init_window()

    def init_window(self):
        self.window = tk.Tk()
        self.window.title("Robot Controller")
        self.window.geometry("400x400")
        self.window.configure(bg="#1e1e2e")

        style = {
            "width": 20,
            "height": 2,
            "bg": "#89b4fa",
            "fg": "black",
            "font": ("Arial", 12, "bold"),
            "relief": tk.RAISED,
            "bd": 4
        }

        stop_style = style.copy()
        stop_style["bg"] = "#f38ba8"
        stop_style["fg"] = "white"

        tk.Label(self.window, text="Control del Robot", font=("Arial", 16), fg="white", bg="#1e1e2e").pack(pady=10)

        # Botones deseados
        tk.Button(self.window, text="↑ move_forward", command=self.move_forward, **style).pack(pady=5)
        tk.Button(self.window, text="← turn_left", command=self.turn_left, **style).pack(pady=5)
        tk.Button(self.window, text="→ turn_right", command=self.turn_right, **style).pack(pady=5)
        tk.Button(self.window, text="↓ move_backward", command=self.move_backward, **style).pack(pady=5)
        tk.Button(self.window, text="⏹️ stop", command=self.stop, **stop_style).pack(pady=15)

        self.window.mainloop()

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 0.15
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info("Adelante")

    def move_backward(self):
        msg = Twist()
        msg.linear.x = -0.15
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info("Atrás")

    def turn_left(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.4
        self.publisher_.publish(msg)
        self.get_logger().info("Girar izquierda")

    def turn_right(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = -0.4
        self.publisher_.publish(msg)
        self.get_logger().info("Girar derecha")

    def stop(self):
        msg = Twist()
        self.publisher_.publish(msg)
        self.get_logger().info("Parado")

def main(args=None):
    rclpy.init(args=args)
    node = RobotControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
