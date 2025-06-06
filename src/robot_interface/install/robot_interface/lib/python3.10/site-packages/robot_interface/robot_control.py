import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2

class RobotControl(Node):
    def __init__(self):
        super().__init__('robot_control')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.update)
        self.get_logger().info("Robot control node started")

        # Configura la cámara
        self.cap = cv2.VideoCapture(0)

    def update(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        
        height, width, _ = frame.shape
        center_y = height // 2

        # Dibuja una línea en el centro
        cv2.line(frame, (0, center_y), (width, center_y), (0, 255, 0), 2)

        # Mostrar la imagen
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)

        # Mover el robot
        msg = Twist()
        if key == ord('w'):  # Adelante
            msg.linear.x = 0.2
        elif key == ord('s'):  # Atrás
            msg.linear.x = -0.2
        else:
            msg.linear.x = 0.0
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.cap.release()
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()
