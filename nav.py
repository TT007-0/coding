#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def send_navigation_goal():
    # 初始化ROS节点
    rospy.init_node('send_navigation_goal', anonymous=True)

    # 创建一个MoveBase动作客户端
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # 等待move_base动作服务器启动
    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()
    rospy.loginfo("MoveBase action server is ready.")

    # 创建一个导航目标
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"  # 目标点所在的坐标系
    goal.target_pose.header.stamp = rospy.Time.now()

    # 设置目标点的位置和姿态
    # 这里的坐标和姿态需要根据实际情况进行修改
    goal.target_pose.pose.position.x = 1.0
    goal.target_pose.pose.position.y = 2.0
    goal.target_pose.pose.position.z = 0.0

    # 目标点的姿态（四元数）
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    # 发送导航目标
    rospy.loginfo("Sending navigation goal...")
    client.send_goal(goal)

    # 等待导航结果
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        result = client.get_result()
        if result:
            rospy.loginfo("Navigation succeeded!")
        else:
            rospy.logerr("Navigation failed!")

if __name__ == '__main__':
    try:
        send_navigation_goal()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation goal sending interrupted.")
