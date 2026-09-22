# Balls Falling Using Real Life Physics

import turtle
import time

# រៀបចំអេក្រង់ (Screen Setup)
screen = turtle.Screen()                                # បង្កើតអេក្រង់
screen.title("មូលដ្ឋានគ្រឹះនៃបាល់លោត (Basic Bouncing Ball)")  # បង្កើតចំណងជើងអេក្រង់
screen.bgcolor("white")                                 # កំណត់ពណ៌ផ្ទៃខាងក្នុង
screen.setup(width=800, height=600)                     # កំណត់ទំហំអេក្រង់

# បង្កើតរូបបាល់
ball = turtle.Turtle()  # បង្កើតរូបបាល់
ball.shape("circle")    # បាល់មានរូបរាងមូល
ball.color("red")       # បាល់មានពណ៌ក្រហម
# ball.penup()            # បញ្ចូលការបញ្ជាក់ថា បាល់មិនចង់គូរ
ball.goto(-250, 100)    # ចាប់ផ្តើមនៅកម្ពស់ ១០០ (Starting at height 100)  x, y

# អថេររូបវិទ្យា (Physics Variables)
vx = 5.0           # ល្បឿនផ្តេក (Horizontal velocity)
vy = 0.0           # ល្បឿនឈរ (Vertical velocity)
gravity = -3    # ទំនាញផែនដី (Downward acceleration)
floor_level = -100 # កម្រិតកម្ពស់កម្រាល (Y-coordinate of floor)

# គូរខ្សែបន្ទាត់កម្រាល
pen = turtle.Turtle()
# pen.hideturtle() # hides arrow
# pen.penup()
pen.goto(-300, floor_level)     # start left
pen.pendown()
pen.pensize(3)
pen.goto(300, floor_level)      # end right

# Loop ត្រាប់តាមរូបវិទ្យា (Simulation Loop)
for _ in range(100): # ដំណើរការ ២០០ ជំហាន
    # 1. បន្ថែមទំនាញផែនដីទៅលើល្បឿនឈរ
    vy += gravity

    # 2. ផ្លាស់ប្តូរទីតាំងបាល់
    ball.setx(ball.xcor() + vx) # -250 += 5.0 (100 Times)
    ball.sety(ball.ycor() + vy) # Balls going downwards
                                # Using vy += gravity (-3) => 100 += (-3) till 0

    # 3. ពិនិត្យការប៉ះទង្គិចជាមួយកម្រាល
    if ball.ycor() <= floor_level: # if the ball touches the floor
        ball.sety(floor_level) # Stop the ball from going through the floor / ទប់កុំឱ្យបាល់លិចចុះក្រោមដី
        vy = -vy * 0.8         # The ball bounces upward at a slightly lower speed at x0.8 per bounce until reaches the end of destination and loop / ប្តូរទិសដៅ និងស្រូបថាមពល (Damping)
        
    time.sleep(0.01) # This pauses for 0.01 seconds between simulation steps.

turtle.done() # បញ្ចប់ការគូរ / Keeps the Turtle window open after the simulation finishes.