from tools import  *
from objects import *
from routines import *


#This file is for strategy

class ExampleBot(GoslingAgent):
    def run(agent):

        close_to_ball = (agent.me.location - agent.ball.location).magnitude() < 2000
        have_boost = agent.me.boost > 20

        my_goal_to_ball, my_ball_distance = (agent.ball.location - agent.friend_goal.location).normalize(True)
        goal_to_me = agent.me.location - agent.friend_goal.location
        my_distance = my_goal_to_ball.dot(goal_to_me)

        """agent.line(agent.friend_goal.location, agent.ball.location, [255, 255, 255])
        my_point = agent.friend_goal.location + (my_goal_to_ball * my_distance)
        agent.line(my_point - Vector3(0,0,100), my_point + Vector3(0,0,100), [0,255,0])"""

        foe_goal_to_ball, foe_ball_distance = (agent.ball.location - agent.foe_goal.location).normalize(True)
        foe_goal_to_foe = agent.foes[0].location - agent.foe_goal.location
        foe_distance = foe_goal_to_ball.dot(foe_goal_to_foe)

        me_onside = my_distance - 200 < my_ball_distance
        foe_onside = foe_distance - 200 < foe_ball_distance




        distance_from_car_to_my_goal = agent.me.location - agent.friend_goal.location
        distance_from_me_to_ball = agent.me.location - agent.ball.location

        distance_from_ball_to_foe_goal = agent.foe_goal.location - agent.ball.location
        distance_from_ball_to_my_goal = agent.friend_goal.location - agent.ball.location

        """if agent.team == 0:
            agent.debug_stack()
            agent.line(agent.foe_goal.location, agent.ball.location, [0, 255, 0]) # Line from enemy goal to ball
            agent.line(agent.friend_goal.location, agent.ball.location, [255, 0, 0]) # Line from my goal to ball"""


        if len(agent.stack) < 1 and len(agent.foes) > 0:
            if agent.kickoff_flag:
                agent.push(kickoff())
            else:
                agent.push(short_shot(agent.foe_goal.location))
