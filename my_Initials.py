
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897 
def movebackward():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
 	vel_msg = Twist()

	speed = 0.5
	
	distance = 2
  	
	vel_msg.linear.x = -abs(speed)

    	vel_msg.linear.y = 0

    	vel_msg.linear.z = 0

    	vel_msg.angular.x = 0

    	vel_msg.angular.y = 0

    	vel_msg.angular.z = 0

       	t0 = rospy.Time.now().to_sec()

      	current_distance = 0

      	while(current_distance < distance):

        	velocity_publisher.publish(vel_msg)

             	t1=rospy.Time.now().to_sec()

        	current_distance= speed*(t1-t0)
	
	vel_msg.linear.x = 0

        velocity_publisher.publish(vel_msg)
def moveforward():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
 	vel_msg = Twist()

	speed = 0.5
	
	distance = 2
  	
	vel_msg.linear.x = abs(speed)

    	vel_msg.linear.y = 0

    	vel_msg.linear.z = 0

    	vel_msg.angular.x = 0

    	vel_msg.angular.y = 0

    	vel_msg.angular.z = 0

       	t0 = rospy.Time.now().to_sec()

      	current_distance = 0

      	while(current_distance < distance):

        	velocity_publisher.publish(vel_msg)

             	t1=rospy.Time.now().to_sec()

        	current_distance= speed*(t1-t0)
	
	vel_msg.linear.x = 0

        velocity_publisher.publish(vel_msg)

def rotateanti():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()		
	speed = 5 	
	angular_speed = speed*2*PI/360
	angle = 90
	relative_angle = angle*2*PI/360
	vel_msg.linear.x=0
  	vel_msg.linear.y=0
  	vel_msg.linear.z=0
  	vel_msg.angular.x = 0
  	vel_msg.angular.y = 0
	vel_msg.angular.z = abs(angular_speed)
	t0 = rospy.Time.now().to_sec()
    	current_angle = 0
	
	while(current_angle < relative_angle):
    		velocity_publisher.publish(vel_msg)
    		t1 = rospy.Time.now().to_sec()
    		current_angle = angular_speed*(t1-t0)
	
	vel_msg.angular.z = 0
  	velocity_publisher.publish(vel_msg)
  	
def rotateclock():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()		
	speed = 5 	
	angular_speed = speed*2*PI/360
	angle = 90
	relative_angle = angle*2*PI/360
	vel_msg.linear.x=0
  	vel_msg.linear.y=0
  	vel_msg.linear.z=0
  	vel_msg.angular.x = 0
  	vel_msg.angular.y = 0
	vel_msg.angular.z = -abs(angular_speed)
	t0 = rospy.Time.now().to_sec()
    	current_angle = 0
	
	while(current_angle < relative_angle):
    		velocity_publisher.publish(vel_msg)
    		t1 = rospy.Time.now().to_sec()
    		current_angle = angular_speed*(t1-t0)
	
	vel_msg.angular.z = 0
  	velocity_publisher.publish(vel_msg)
  	
   

         
   
  
      	

 

if __name__ == '__main__':

  try:
  	movebackward()
	rotateclock()
	moveforward()
	rotateanti()
	moveforward()
	rotateclock()
	moveforward()
	rotateclock()
	moveforward()
  except rospy.ROSInterruptException: pass
