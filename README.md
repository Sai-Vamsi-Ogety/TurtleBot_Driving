# TurtleBot_Driving
Make the TurtleBot move in a desired way.

Quick Overview of Graph Concepts

Nodes: A node is an executable that uses ROS to communicate with other nodes.

Messages: ROS data type used when subscribing or publishing to a topic.

Topics: Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.

Master: Name service for ROS (i.e. helps nodes find each other)

rosout: ROS equivalent of stdout/stderr

roscore: Master + rosout + parameter server

We Define four Methods namely : MoveForward, MoveBackward, RotateClockwise, RotateAnticlockwise

We Initialize Rosnode(Our TurtleBot) and Publish messages to '/turtle1/cmd_vel' topic 
