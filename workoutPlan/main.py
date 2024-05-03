from customtkinter import *
from PIL import Image
import time
import os
window = CTk()
window._set_appearance_mode('dark')
window.geometry('800x500')
window.resizable(False, False)
window.title('FitTracker')

# -----------------calculate bmi-----------------
# def BMI():
#     try:
#         x = eval(weight.get())
#         z = eval(height.get() + '/100')
#         a = z ** 2
#         bmi = round(x / a, 2)
#         L1.configure(text=f'BMI - {bmi}')
#         if bmi < 16:
#             L2.configure(text='Severe Thinness')
#         if bmi >= 16 and bmi < 17:
#             L2.configure(text='Moderate Thinness')
#         if bmi >= 17 and bmi < 18.5:
#             L2.configure(text='Mild thinness')
#         if bmi >= 18.5 and bmi < 25:
#             L2.configure(text='Normal')
#         if bmi >= 25 and bmi < 30:
#             L2.configure(text='Overweight')
#         if bmi >= 30 and bmi < 35:
#             L2.configure(text='Obese Class 1')
#         if bmi >= 35 and bmi < 40:
#             L2.configure(text='Obese Class 2')
#         if bmi >= 40:
#             L2.configure(text='Obese Class 3')
#     except NameError:
#         L1.configure(text='Invalid Input!')
#         L2.configure(text='')
#     weight.delete(0, END)
#     height.delete(0, END)

# ------------------------button1-fat-loss-plan----------------------
def but1():
    fat_frame = CTkFrame(window, width=800, height=500, fg_color='#EB6A00')
    fat_frame.place(x=0, y=0)
    fat_frame.pack_propagate(False)
    FF1 = CTkFrame(fat_frame, height=501, width=520, fg_color='#1E1F22', corner_radius=0)
    FF1.place(x=281, y=0)
    FF1.pack_propagate(False)
    fat = Image.open(os.path.join(os.path.dirname(__file__),'fat.png'))
    fat_img = CTkImage(dark_image=fat, size=(370, 500))
    fat_label = CTkLabel(FF1, text='', image=fat_img)
    fat_label.pack()
    back_but = CTkButton(FF1, text='<Back', font=('open sans', 15),
                              fg_color='#1E1F22', hover_color='#1E1F22', text_color='#EB6A00', cursor='hand2',
                              command=lambda: fat_frame.destroy())
    back_but.place(x=0, y=0)
    f11_label = CTkLabel(FF1, text='', font=('open sans', 20, 'underline'), text_color='#EB6A00')
    f11_label.pack(padx=5, pady=5)
    f12_label = CTkLabel(FF1, text='', font=('open', 15), text_color='white')
    f12_label.pack()

    def f1():
        fat_label.destroy()
        f11_label.configure(text='JUMPING JACKS')
        f12_label.configure(text='''
    JUMPING JACKS - 3 minutes
    TIPS - 
    1.Form: Keep your back straight, land softly, and ensure
    your knees are slightly bent to reduce impact.

    2.Tighten your abdominal muscles
    to enhance the benefits for your core.

    3.Controlled Breathing: Breathe rhythmically to
     maintain stamina and prevent fatigue.

    4.Beginners can start with a lower intensity
     and gradually increase as fitness improves.

    -They are an excellent calorie-burning exercise.

    -require no special equipment and can be done almost anywhere.

    3 minutes calories burnt : 30 calories''')

    def f2():
        fat_label.destroy()
        f11_label.configure(text='HIGH KNEES')
        f12_label.configure(text='''
    HIGH KNEES - 2 minutes
    TIPS-
    1.Form: Lift your knees as high as comfortable,
    land softly, and keep your back straight.

    2.Engage Core Muscles: Tighten your abdominal muscles 
    throughout the exercise to maximize the benefits for your core.
    3.Arm Movement: Swing your arms in a coordinated 
    manner to enhance the overall intensity.

    4.Pace Yourself: Start at a manageable pace and gradually
    increase the intensity as your fitness level improves.

    -High knees are a high-intensity exercise that can contribute
    to calorie expenditure, aiding in weight management.

    -Leg Strength: High knees engage the muscles of the
     lower body, including the quadriceps, hamstrings, and calves.

    2 minutes calories burnt : 20 calories''')

    def f3():
        fat_label.destroy()
        f11_label.configure(text='BURPEES')
        f12_label.configure(text='''
    BURPEES - 3 sets (10-15 reps)
    TIPS-
    1.Maintain Proper Form: Start in a squat position, jump back
    into a plank,perform a push-up, jump back to a squat, and
    explosively jump up. Keep your back straight, and ensure
    your movements are controlled.

    2.Engage Core Muscles: Tighten your core throughout the 
    exercise to provide stability and protect your lower back.

    3.Controlled Landing: Land softly to reduce impact on 
    your joints, especially your knees.

    4.Consistent Pace:Find a pace that challenges you but allows for 
    proper form.Burpees are about quality over quantity,
    especially when starting.

    Burpees engage multiple muscle groups, including chest, arms,
    legs, core, and shoulders.

    Burpees elevate the heart rate, providing an effective cardiovascular workout

    3 sets of 10-15 reps : 30-45 calories.''')

    def f4():
        fat_label.destroy()
        f11_label.configure(text='JUMP SQUATS')
        f12_label.configure(text='''
    JUMP SQUATS -  3 sets (10-15 reps)
    TIPS- 
    1.Proper Form:Start with your feet shoulder-width apart.
    Lower your body into a squat position, then explosively
    jump up, reaching for the sky.Land softly, bending your
    knees to absorb the impact.

    2.Engage Core Muscles:Tighten your core throughout the exercise
    to stabilize your body and protect your lower back.

    3.Controlled Movements:Focus on controlled movements,
    especially during the landing phase.
    Avoid letting your knees collapse inward.

    4.Consistent Pace:Find a pace that challenges you
    but allows for proper form.You can adjust the intensity
    by modifying the height of your jumps.

    - Jump squats primarily target the muscles of the lower body,
    They help improve leg strength and power.

    - This exercise engages not only the lower body but also the
    core and stabilizing muscles throughout the body.''')

    def f5():
        fat_label.destroy()
        f11_label.configure(text='MOUNTAIN CLIMBERS')
        f12_label.configure(text='''
    MOUNTAIN CLIMBERS - 3 sets (30 seconds)
    TIPS-
    1.Proper Form: Start in a plank position with your wrists 
    directly under your shoulders.Bring your knees toward your 
    chest one at a time in a controlled manner.

    2.Engage Core Muscles: Keep your core muscles tight throughout
    he exercise to maintain stability.

    3. Controlled Movements:Focus on controlled movements, avoiding
    excessive bouncing or momentum.

    4.Incorporate into Workouts: Use mountain climbers as part of a 
    warm-up, high-intensity interval training (HIIT) routine, or 
    as a cardio element in your workout.

    - Mountain climbers elevate the heart rate, providing cardiovascular
    benefits and improving endurance.

    - The constant engagement of the core muscles helps improve abdominal
    strength and stability.

    3 sets of 30 seconds: 22.5 calories''')

    def f6():
        fat_label.destroy()
        f11_label.configure(text='PLANK')
        f12_label.configure(text='''
    PLANK - 3 sets (30-50 seconds)
    TIPS-

    1.Proper Form:Start in a plank position with your hands directly beneath
    your shoulders and your body forming a straight line from head to heels.
    Engage your core and avoid sagging or arching your back.

    2.Steady Breathing:Maintain steady breathing throughout the plank
    to avoid unnecessary tension.

    3.Gradual Progression:If you're a beginner, start with shorter 
    durations and gradually increase the time as your strength improves.

    4.Consistent Practice:Aim for regular plank sessions to build
    endurance and strength over time.

    - Core Strength:The plank is highly effective for strengthening the
     muscles of the core.

    - Stability and Posture:Holding a plank position helps improve overall
    stability and posture by engaging the muscles that support the spine.

    3 sets of 30-50 seconds: 10-20 calories''')

    def f7():
        fat_label.destroy()
        f11_label.configure(text='LUNGES')
        f12_label.configure(text='''
    LUNGES - 3 sets (10-15 reps each leg)
    TIPS-
    1.Proper Form:Stand with feet hip-width apart, take a step forward or
    backward, and lower your body until both knees are bent at a 90-degree 
    angle.Keep your front knee directly above your ankle and ensure your
    back knee hovers just above the floor.

    2.Engage Core Muscles:Tighten your core to stabilize your body
    throughout the movement.

    3.Consistent Pace:Maintain a consistent pace, and if using added resistance
    (like dumbbells), choose a weight that allows for proper form.

    4.Gradual Progression:Start with a number of reps that challenge you without
     sacrificing form and gradually increase the intensity as your strength improves
    - Lunges primarily target the muscles of the quadriceps, hamstrings,
    and glutes, helping to build strength and endurance.

    - Lunges require balance and stability, engaging the core
    muscles and improving overall balance.

    3 sets of 10-15 reps - 70 calories''')

    def f8():
        fat_label.destroy()
        f11_label.configure(text='SQUATS')
        f12_label.configure(text='''
    SQUATS - 3 sets (15-20 reps)
    TIPS-
    1.Proper Form:Stand with your feet shoulder-width apart, toes pointing
    slightly outward.Lower your body by bending at the hips and knees,
    keeping your back straight and chest up.Aim to lower your hips until
    your thighs are parallel to the ground.

    2.Engage Core Muscles:Tighten your core to stabilize your spine and
    prevent lower back strain.

    3.Controlled Movements:Perform squats with controlled, deliberate
    movements, avoiding bouncing or jerking.

    4.Full Range of Motion:Lower your body to a depth that allows for a full
     range of motion, ensuring that your knees do not go past your toes.

    - Squats are highly effective for building strength in the muscles of 
    the thighs and lower body.

    - Squats specifically target the gluteal muscles, contributing to
    improved shape and strength of the buttocks.

    3 sets of 15-20 reps: 100-150 calories''')

    def f9():
        fat_label.destroy()
        f11_label.configure(text='BOX JUMPS')
        f12_label.configure(text='''
    BOX JUMPS - 3 sets (10-15 reps)
    TIPS-
    1.Proper Form:Stand in front of the box with your feet shoulder-width apart.
    Bend at the hips and knees, swinging your arms back, then explode upward
    to land on the box with both feet.

    2.Land Softly:Focus on a soft and controlled landing to reduce impact
    on the joints.

    3.Full Extension:Fully extend your hips and knees at the top of the jump
    to maximize the engagement of leg muscles.

    4.Safety First:Choose a box height that is appropriate for your fitness
    level.
    Ensure that the box is stable and placed on a flat surface.

    - Box jumps primarily target the muscles in the lower body, including the
    quadriceps, hamstrings, glutes, and calves.

    - Box jumps require a quick and explosive movement, promoting power
    development in the legs.

    3 sets of 10-15 reps: 60-150 calories''')

    def f10():
        fat_label.destroy()
        f11_label.configure(text='COBRA STRETCHING')
        f12_label.configure(text='''
    COBRA STRETCHING  - 2 sets (20-30 seconds)
    TIPS-
    1.Proper Form:Lie on your stomach with your palms on the floor beneath
    your shoulders.
    Press the tops of your feet into the mat and lift your chest,
    keeping your elbows slightly bent.

    2.Engage Core Muscles:Tighten your abdominal muscles to support the 
    lower back and prevent excessive arching.

    3.Relax Shoulders:Allow your shoulders to relax away from your ears,
    and maintain a gentle stretch in the lower back.

    4.Breathe Deeply:Focus on deep, diaphragmatic breathing to enhance
    relaxation and deepen the stretch.

    - The Cobra Stretch helps improve flexibility in the spine,
    particularly in the lower back.

    - Regular practice of the Cobra Stretch can contribute to
    better posture by opening up the chest and shoulders.''')

    F1 = CTkButton(fat_frame, text='1. Jumping Jacks -  3 minutes ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f1)
    F1.pack(anchor='w')
    F2 = CTkButton(fat_frame, text='2. High Knees - 2 minutes ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f2)
    F2.pack(anchor='w')
    F3 = CTkButton(fat_frame, text='3. Burpees - 3 sets (10-15 reps) ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f3)
    F3.pack(anchor='w')
    F4 = CTkButton(fat_frame, text='4. Jump Squats -  3 sets (10-15 reps) ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f4)
    F4.pack(anchor='w')
    F5 = CTkButton(fat_frame, text='5. Mountain climbers - 3 sets (30 seconds)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f5)
    F5.pack(anchor='w')
    F6 = CTkButton(fat_frame, text='6. Plank - 3 sets (30-50 seconds)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f6)
    F6.pack(anchor='w')
    F7 = CTkButton(fat_frame, text='7. Lunges - 3 sets (10-15 reps each leg)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f7)
    F7.pack(anchor='w')
    F8 = CTkButton(fat_frame, text='8. Squats - 3 sets (15-20 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f8)
    F8.pack(anchor='w')
    F9 = CTkButton(fat_frame, text='9. Box jumps - 3 sets (10-15 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f9)
    F9.pack(anchor='w')
    F10 = CTkButton(fat_frame, text='10. Cobra Stretching  - 2 sets (20-30 seconds)', width=280, height=50,
                    corner_radius=0, fg_color='#1E1F22', command=f10)
    F10.pack(anchor='w')

# ------------------------------------button-muscle-gain-plan----------
def but2():
    muscle_frame = CTkFrame(window, width=800, height=500, fg_color='#EB6A00')
    muscle_frame.place(x=0, y=0)
    muscle_frame.pack_propagate(False)
    FF1 = CTkFrame(muscle_frame, height=501, width=520, fg_color='#1E1F22', corner_radius=0)
    FF1.place(x=281, y=0)
    FF1.pack_propagate(False)
    fat = Image.open(os.path.join(os.path.dirname(__file__),'fat2.png'))
    fat_img = CTkImage(dark_image=fat, size=(370, 500))
    fat_label = CTkLabel(FF1, text='', image=fat_img)
    fat_label.pack()
    back_but = CTkButton(FF1, text='<Back', font=('open sans', 15), fg_color='#1E1F22',
                         hover_color='#1E1F22', text_color='#EB6A00', cursor='hand2',
                         command=lambda: muscle_frame.destroy())
    back_but.place(x=0, y=0)
    f11_label = CTkLabel(FF1, text='', font=('open sans', 20, 'underline'), text_color='#EB6A00')
    f11_label.pack(padx=5, pady=5)
    f12_label = CTkLabel(FF1, text='', font=('open', 15), text_color='white')
    f12_label.pack()

    def f1():
        fat_label.destroy()
        f11_label.configure(text='JUMPING JACKS')
        f12_label.configure(text='''
        JUMPING JACKS - 3 minutes
        TIPS - 
        1.Form: Keep your back straight, land softly, and ensure
        your knees are slightly bent to reduce impact.

        2.Tighten your abdominal muscles
        to enhance the benefits for your core.

        3.Controlled Breathing: Breathe rhythmically to
         maintain stamina and prevent fatigue.

        4.Beginners can start with a lower intensity
         and gradually increase as fitness improves.

        -They are an excellent calorie-burning exercise.

        -require no special equipment and can be done almost anywhere.

        3 minutes calories burnt : 30 calories''')

    def f2():
        fat_label.destroy()
        f11_label.configure(text='PUSH UPS')
        f12_label.configure(text='''
    PUSH UPS - 5 sets (10-12 reps)
    TIPS-   
    1.Proper Form:Start in a plank position with hands slightly wider than
    shoulder-width apart.Lower your body to the ground by bending your elbows,
    keeping your body in a straight line.

    2.Engage Core Muscles:Tighten your core to maintain a straight body
    throughout the movement.

    3.Full Range of Motion:Aim to lower your chest close to the ground
     for a full range of motion.

    4. Controlled Movements:Perform push-ups with controlled and deliberate
    movements,avoiding rapid or jerky motions.

    - Push-ups are effective for building strength in the chest, shoulders,
    and triceps.

    - The plank position during push-ups engages the core muscles,
    contributing to core strength and stability.

    5 sets of 10-12 reps: 130-150 calories

    Note: if these variation seems hard for you you can bend your knees and 
    perfom the same movements''')

    def f3():
        fat_label.destroy()
        f11_label.configure(text='DIAMOND PUSH UPS')
        f12_label.configure(text='''
    DIAMOND PUSH UPS - 5 sets (5-10 reps)
    TIPS-
    1.Proper Form:Start in a plank position with your hands close together,
    forming a diamond shape with your thumbs and index fingers.Lower your
    chest toward the diamond shape on the ground and push back up.

    2.Engage Core Muscles:Tighten your core to maintain a straight body 
    throughout the movement.

    3.Full Range of Motion:

    4.Aim to lower your chest close to the diamond shape on the ground
    for a full range of motion.

    - Diamond push-ups target the triceps more intensively compared
    to standard push-ups.

    - This variation places increased emphasis on the inner chest muscles.

    5 sets of 10-12 reps: 100-130 calories
    Note: if these variation seems hard for you you can bend your knees and 
    perfom the same movements''')

    def f4():
        fat_label.destroy()
        f11_label.configure(text='PIKE PUSH UPS')
        f12_label.configure(text='''
    PIKE PUSH UPS -  3 sets (8-12 reps)
    TIPS- 
    1.Proper Form:Start in a plank position with your hands placed directly
    beneath your shoulders.Lift your hips toward the ceiling, forming an
    inverted V shape with your body.Lower your head toward the ground and
    press back up.

    2.Engage Core Muscles:Tighten your core to maintain a straight line 
    from your head to your heels.

    3.Full Range of Motion:Aim to lower your head toward the ground for
    a full range of motion.

    4.Controlled Movements:Perform pike push-ups with controlled and
    deliberate movements,avoiding rapid or jerky motions.

    - Pike push-ups target the shoulders more intensely compared
    to standard push-ups.

    - This variation engages the upper part of the chest,
    contributing to a well-rounded chest workout.

    3 sets of 8-12 reps: 40-60 calories
    Note: if these variation seems hard for you you can bend your knees and 
    perfom the same movements''')

    def f5():
        fat_label.destroy()
        f11_label.configure(text='CRUNCHES')
        f12_label.configure(text='''
    CRUNCHES - 3 sets (30 reps)
    TIPS-  
    1.Proper Form:Lie on your back with your knees bent and feet flat on the floor.
    Place your hands behind your head or across your chest.
    Lift your upper body toward your knees, engaging your abdominal muscles.

    2.Engage Core Muscles:Focus on contracting your abdominal muscles
    throughout the movement.

    3.Breathing:Exhale as you lift your upper body and inhale as
    you lower it back down.

    4.Avoid Neck Strain:Keep your neck in a neutral position to avoid
     strain. Avoid pulling on your head or neck with your hands.

    - Crunches are effective for strengthening the muscles
     of the abdominal wall, including the rectus abdominis.

    - Strengthening the core muscles can contribute to better posture 
    and spinal alignment.

    3 sets of 30 reps: 30-60 calories
        ''')

    def f6():
        fat_label.destroy()
        f11_label.configure(text='LEG RAISES')
        f12_label.configure(text='''
    LEG RAISES 3 sets (15-20 reps)
    TIPS-
    1.Proper Form:Lie on your back with your legs straight and arms
    by your sides. Lift your legs toward the ceiling, keeping them straight,
    and lower them back down without letting them touch the ground.

    2.Engage Core Muscles:Focus on contracting your abdominal muscles
    throughout the movement.

    3.Breathing:Exhale as you lift your legs and inhale as you lower
    them back down.

    4.Controlled Movements:Perform leg raises with controlled and
    deliberate movements, avoiding rapid or jerky motions.

    - Leg raises are effective for strengthening the muscles of
    the lower abdomen, particularly the rectus abdominis.

    - The exercise engages the hip flexors, contributing
    to overall core strength.

    3 sets of 15-20 reps: 45-120 calories
    Note: if this variation is seems tough bend your
     knees and do the same movements
    ''')

    def f7():
        fat_label.destroy()
        f11_label.configure(text='SQUATS')
        f12_label.configure(text='''
    SQUATS - 3 sets (20 reps)
    TIPS-
    1.Proper Form:Stand with your feet shoulder-width apart, toes pointing
    slightly outward.Lower your body by bending at the hips and knees,
    keeping your back straight and chest up.Aim to lower your hips until
    your thighs are parallel to the ground.

    2.Engage Core Muscles:Tighten your core to stabilize your spine and
    prevent lower back strain.

    3.Controlled Movements:Perform squats with controlled, deliberate
    movements, avoiding bouncing or jerking.

    4.Full Range of Motion:Lower your body to a depth that allows for a full
    range of motion, ensuring that your knees do not go past your toes.

    - Squats are highly effective for building strength in the muscles of 
    the thighs and lower body.

    - Squats specifically target the gluteal muscles, contributing to
    improved shape and strength of the buttocks.

    3 sets of 20 reps: 130-150 calories''')

    def f8():
        fat_label.destroy()
        f11_label.configure(text='BURPEES')
        f12_label.configure(text='''
    BURPEES - 3 sets (10-15 reps)
    TIPS-
    1.Maintain Proper Form: Start in a squat position, jump back
    into a plank,perform a push-up, jump back to a squat, and
    explosively jump up. Keep your back straight, and ensure
    your movements are controlled.

    2.Engage Core Muscles: Tighten your core throughout the 
    exercise to provide stability and protect your lower back.

    3.Controlled Landing: Land softly to reduce impact on 
    your joints, especially your knees.

    4.Consistent Pace:Find a pace that challenges you but allows for 
    proper form.Burpees are about quality over quantity,
    especially when starting.

    - Burpees engage multiple muscle groups, including chest, arms,
    legs, core, and shoulders.

    - Burpees elevate the heart rate, providing an effective cardiovascular workout

    3 sets of 10-15 reps : 30-45 calories.''')

    def f9():
        fat_label.destroy()
        f11_label.configure(text='PLANK')
        f12_label.configure(text='''
    PLANK - 3 sets (1 minute)
    TIPS-
    1.Proper Form:Start in a plank position with your hands directly beneath
    your shoulders and your body forming a straight line from head to heels.
    Engage your core and avoid sagging or arching your back.

    2.Steady Breathing:Maintain steady breathing throughout the plank
    to avoid unnecessary tension.

    3.Gradual Progression:If you're a beginner, start with shorter 
    durations and gradually increase the time as your strength improves.

    4.Consistent Practice:Aim for regular plank sessions to build
    endurance and strength over time.

    - Core Strength:The plank is highly effective for strengthening the
    muscles of the core.

    - Stability and Posture:Holding a plank position helps improve overall
    stability and posture by engaging the muscles that support the spine.

    3 sets of 1 minute: 20-30 calories''')

    def f10():
        fat_label.destroy()
        f11_label.configure(text='Cobra Stretching')
        f12_label.configure(text='''
    COBRA STRETCHING  - 2 sets (20-30 seconds)
    TIPS-
    1.Proper Form:Lie on your stomach with your palms on the floor beneath
    your shoulders.
    Press the tops of your feet into the mat and lift your chest,
    keeping your elbows slightly bent.

    2.Engage Core Muscles:Tighten your abdominal muscles to support the 
    lower back and prevent excessive arching.

    3.Relax Shoulders:Allow your shoulders to relax away from your ears,
    and maintain a gentle stretch in the lower back.

    4.Breathe Deeply:Focus on deep, diaphragmatic breathing to enhance
    relaxation and deepen the stretch.

    - The Cobra Stretch helps improve flexibility in the spine,
    particularly in the lower back.

    - Regular practice of the Cobra Stretch can contribute to
    better posture by opening up the chest and shoulders.''')

    F1 = CTkButton(muscle_frame, text='1. Warmup - Jumping Jacks -  3 minutes ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f1)
    F1.pack(anchor='w')
    F2 = CTkButton(muscle_frame, text='2. Push Ups - 5 sets (10-12 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f2)
    F2.pack(anchor='w')
    F3 = CTkButton(muscle_frame, text='3. Dimond Push Ups - 5 sets (5-10 reps) ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f3)
    F3.pack(anchor='w')
    F4 = CTkButton(muscle_frame, text='4. Pike Push Ups -  3 sets (8-12 reps) ', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f4)
    F4.pack(anchor='w')
    F5 = CTkButton(muscle_frame, text='5. Crunches - 3 sets (30 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f5)
    F5.pack(anchor='w')
    F6 = CTkButton(muscle_frame, text='6. Leg Raises 3 sets (15-20 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f6)
    F6.pack(anchor='w')
    F7 = CTkButton(muscle_frame, text='7. Squats - 3 sets (20 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f7)
    F7.pack(anchor='w')
    F8 = CTkButton(muscle_frame, text='8. Burpees - 3 sets (10-15 reps)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f8)
    F8.pack(anchor='w')
    F9 = CTkButton(muscle_frame, text='9. Plank - 2 sets (1 minute)', width=280, height=50,
                   corner_radius=0, fg_color='#1E1F22', command=f9)
    F9.pack(anchor='w')
    F10 = CTkButton(muscle_frame, text='10. Cobra Stretching  - 2 sets (20-30 seconds)', width=280, height=50,
                    corner_radius=0, fg_color='#1E1F22', command=f10)
    F10.pack(anchor='w')

# ---------------------------------button-fat-diet------------------------
def but3():
    fat_diet_frame = CTkFrame(window, width=800, height=500, fg_color='#EB6A00')
    fat_diet_frame.place(x=0, y=0)
    fat_diet_frame.pack_propagate(False)
    FF1 = CTkFrame(fat_diet_frame, height=501, width=520, fg_color='#1E1F22', corner_radius=0)
    FF1.place(x=281, y=0)
    FF1.pack_propagate(False)
    diet1 = Image.open(os.path.join(os.path.dirname(__file__),'diet1.png'))
    diet1_img = CTkImage(dark_image=diet1, size=(370, 500))
    diet1_label = CTkLabel(FF1, text='', image=diet1_img)
    diet1_label.pack()
    back_but = CTkButton(FF1, text='<Back', font=('open sans', 15), fg_color='#1E1F22',
                         hover_color='#1E1F22', text_color='#EB6A00', cursor='hand2',
                         command=lambda: fat_diet_frame.destroy())
    back_but.place(x=0, y=0)
    f11_label = CTkLabel(FF1, text='', font=('open sans', 20, 'underline'), text_color='#EB6A00')
    f11_label.pack(padx=5, pady=5)
    f12_label = CTkLabel(FF1, text='', font=('open', 15), text_color='white')
    f12_label.pack()

    def f1():
        diet1_label.destroy()
        f11_label.configure(text='BREAKFAST')
        f12_label.configure(text='''
Poha:

Ingredients:

1. 1 cup flattened rice (poha)
2. 1 tablespoon oil
3. Mustard seeds, cumin seeds, curry leaves
4. 1 onion, finely chopped
5. 1/2 cup peas and carrots

Turmeric, salt, lemon juice
Instructions:

STEPS:
Rinse poha and set aside.
In a pan, heat oil, add mustard seeds, cumin seeds, and curry leaves.
Add chopped onion, peas, and carrots. Sauté until vegetables are tender.
Add turmeric, salt, and rinsed poha. Mix well.
Cook for a few minutes, squeeze lemon juice, and serve.
Estimated Calories: Approximately 250-300 calories per serving.''')

    def f2():
        diet1_label.destroy()
        f11_label.configure(text='MID MORNING SNACK')
        f12_label.configure(text='''
Greek Yogurt with Almonds:

Ingredients:

1. 1 cup Greek yogurt
2. Handful of almonds (soaked overnight)
3. Honey (optional)

Instructions:

Mix Greek yogurt with soaked almonds.
Optionally, drizzle honey on top.
Estimated Calories: Approximately 150-200 calories per serving.''')

    def f3():
        diet1_label.destroy()
        f11_label.configure(text='LUNCH')
        f12_label.configure(text='''
Roti with Dal and Sabzi:

Ingredients:

1. 2 whole wheat rotis
2. 1 cup lentil dal
3. Mixed vegetable sabzi
4. Cucumber raita
Instructions:

Serve two whole wheat rotis with lentil dal and mixed vegetable sabzi.
Accompany with cucumber raita.
Estimated Calories: Approximately 400-500 calories per serving.''')

    def f4():
        diet1_label.destroy()
        f11_label.configure(text='EVENING SNACKS')
        f12_label.configure(text='''
Sprouts Salad:

Ingredients:

1. Mixed sprouts
2. Onion, tomato, cucumber
3. Chaat masala, lemon juice

Instructions:

Mix sprouts with chopped veggies, chaat masala, and lemon juice.
Toss well and serve.
Estimated Calories: Approximately 150-200 calories per serving.''')

    def f5():
        diet1_label.destroy()
        f11_label.configure(text='DINNER')
        f12_label.configure(text='''
Grilled Chicken/Fish with Roti:

Ingredients:

1. Grilled chicken or fish fillet
2. 2 whole wheat rotis
3. Mixed green salad
4. Instructions:

Grill chicken or fish, serve with whole wheat rotis and a side salad.
Estimated Calories: Approximately 400-500 calories per serving.''')

    def f6():
        diet1_label.destroy()
        f11_label.configure(text='BEFORE BED')
        f12_label.configure(text='''
Turmeric Milk:

Ingredients:

1. 1 cup warm milk
2. Turmeric powder
3. Cinnamon (optional)

Instructions:

Mix turmeric powder into warm milk.
Add a pinch of cinnamon if desired.
Estimated Calories: Approximately 100-150 calories per serving.''')

    F1 = CTkButton(fat_diet_frame, text='1.Breakfast', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f1)
    F1.pack(anchor='w', padx=0, pady=0)
    F2 = CTkButton(fat_diet_frame, text='2.Mid Morning snack', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f2)
    F2.pack(anchor='w', padx=0, pady=0)
    F3 = CTkButton(fat_diet_frame, text='3.Lunch', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f3)
    F3.pack(anchor='w', padx=0, pady=0)
    F4 = CTkButton(fat_diet_frame, text='4.Evening Snacks', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f4)
    F4.pack(anchor='w', padx=0, pady=0)
    F5 = CTkButton(fat_diet_frame, text='5.Dinner', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f5)
    F5.pack(anchor='w', padx=0, pady=0)
    F6 = CTkButton(fat_diet_frame, text='6.Before bed', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f6)
    F6.pack(anchor='w', padx=0, pady=0)

# -----------------------button-muscle-diet------------------
def but4():
    muscle_diet_frame = CTkFrame(window, width=800, height=500, fg_color='#EB6A00')
    muscle_diet_frame.place(x=0, y=0)
    muscle_diet_frame.pack_propagate(False)
    FF1 = CTkFrame(muscle_diet_frame, height=501, width=520, fg_color='#1E1F22', corner_radius=0)
    FF1.place(x=281, y=0)
    FF1.pack_propagate(False)
    diet2 = Image.open(os.path.join(os.path.dirname(__file__),'diet2.png'))
    diet2_img = CTkImage(dark_image=diet2, size=(370, 500))
    diet2_label = CTkLabel(FF1, text='', image=diet2_img)
    diet2_label.pack()
    back_but = CTkButton(FF1, text='<Back', font=('open sans', 15), fg_color='#1E1F22',
                         hover_color='#1E1F22', text_color='#EB6A00', cursor='hand2',
                         command=lambda: muscle_diet_frame.destroy())
    back_but.place(x=0, y=0)
    f11_label = CTkLabel(FF1, text='', font=('open sans', 20, 'underline'), text_color='#EB6A00')
    f11_label.pack(padx=5, pady=5)
    f12_label = CTkLabel(FF1, text='', font=('open', 15), text_color='white')
    f12_label.pack()

    def f1():
        diet2_label.destroy()
        f11_label.configure(text='BREAKFAST')
        f12_label.configure(text='''
Oats and Banana Smoothie:

Ingredients:

1. 1 cup rolled oats
2. 1 banana
3. 1 cup milk (dairy or plant-based)
4. 1 tablespoon peanut butter
Honey (optional)
Instructions:

Blend rolled oats, banana, milk, and peanut butter until smooth.
Optionally, add honey for sweetness.
Estimated Calories: Approximately 400-500 calories''')

    def f2():
        diet2_label.destroy()
        f11_label.configure(text='MID MORNING SNACK')
        f12_label.configure(text='''
Greek Yogurt with Mixed Nuts:

Ingredients:

1. 1 cup Greek yogurt
2. Almonds, walnuts, and pistachios
3. Honey (optional)
Instructions:

Mix Greek yogurt with a variety of mixed nuts.
Optionally, add honey for sweetness.
Estimated Calories: Approximately 300-400 calories''')

    def f3():
        diet2_label.destroy()
        f11_label.configure(text='LUNCH')
        f12_label.configure(text='''
Chicken or Lentil Curry with Brown Rice:

Ingredients:

1. Chicken breast or lentils
2. Onion, tomatoes, ginger, garlic
3. Spices: garam masala, cumin, coriander
4. Brown rice
Instructions:

Cook chicken or lentils in a curry with onions,
tomatoes, and spices.
Serve with brown rice.
Estimated Calories: Approximately 600-800 calories''')

    def f4():
        diet2_label.destroy()
        f11_label.configure(text='EVENING SNACK')
        f12_label.configure(text='''
Chickpea Chaat:

Ingredients:

1. Boiled chickpeas
2. Chopped onions, tomatoes, cucumber
3. Chaat masala, lemon juice
Instructions:

Mix boiled chickpeas with chopped veggies, chaat
masala, and lemon juice.
Estimated Calories: Approximately 300-400 calories''')

    def f5():
        diet2_label.destroy()
        f11_label.configure(text='DINNER')
        f12_label.configure(text='''
Grilled Salmon with Quinoa:

Ingredients:

1. Salmon fillet
2. Quinoa
3. Steamed broccoli
4. Olive oil, garlic, and herbs for seasoning
Instructions:

Season salmon with herbs, grill until cooked.
Serve with quinoa and steamed broccoli.
Estimated Calories: Approximately 600-800 calories''')

    def f6():
        diet2_label.destroy()
        f11_label.configure(text='BEFORE BED')
        f12_label.configure(text='''
Cottage Cheese (Paneer) Snack:

Ingredients:

1. Paneer cubes
2. Cherry tomatoes
3. Basil leaves
4. Olive oil drizzle
Instructions:

Skewer paneer cubes, cherry tomatoes, and basil leaves.
Drizzle with olive oil.
Estimated Calories: Approximately 200-300 calories''')

    F1 = CTkButton(muscle_diet_frame, text='1.Breakfast', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f1)
    F1.pack(anchor='w', padx=0, pady=0)
    F2 = CTkButton(muscle_diet_frame, text='2.Mid Morning snack', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f2)
    F2.pack(anchor='w', padx=0, pady=0)
    F3 = CTkButton(muscle_diet_frame, text='3.Lunch', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f3)
    F3.pack(anchor='w', padx=0, pady=0)
    F4 = CTkButton(muscle_diet_frame, text='4.Evening Snacks', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f4)
    F4.pack(anchor='w', padx=0, pady=0)
    F5 = CTkButton(muscle_diet_frame, text='5.Dinner', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f5)
    F5.pack(anchor='w', padx=0, pady=0)
    F6 = CTkButton(muscle_diet_frame, text='6.Before bed', width=280, height=84,
                   corner_radius=0, fg_color='#1E1F22', command=f6)
    F6.pack(anchor='w', padx=0, pady=0)


# -------------method for plans button-------------------
def Plans():
    plans.configure(state='disabled')
    progressbar = CTkProgressBar(fr1,
                                 width=200,
                                 height=20,
                                 border_width=2,
                                 fg_color='#EBEBEB',
                                 progress_color='#EB6A00')
    progressbar.pack(padx=15, pady=15)

    i = 0
    for i in range(101):
        window.update()
        i /= 100
        progressbar.set(i)
        time.sleep(0.02)
    if i == 1.0:
        progressbar.destroy()
    global fr2
    fr2 = CTkFrame(window, width=800, height=500, fg_color='#EB6A00')
    fr2.place(x=0, y=0)
    fr2.pack_propagate(False)
    # ---------------button images-----------

    b1 = Image.open(os.path.join(os.path.dirname(__file__),'b1.png'))
    b1_img = CTkImage(dark_image=b1, size=(390, 242))
    B1 = CTkButton(fr2, text='', font=('open sans', 30), width=200, height=251, corner_radius=0,
                   image=b1_img, border_width=0, fg_color='#1E1F22', hover_color='#EB6A00',
                   cursor='hand2', command=but1)
    B1.grid()
    b2 = Image.open(os.path.join(os.path.dirname(__file__),'b2.png'))
    b2_img = CTkImage(dark_image=b2, size=(390, 242))
    B2 = CTkButton(fr2, text='', font=('open sans', 30), width=200, height=251, corner_radius=0,
                   image=b2_img, border_width=0, fg_color='#1E1F22', hover_color='#EB6A00',
                   cursor='hand2', command=but2)
    B2.grid(row=0, column=1)
    b3 = Image.open(os.path.join(os.path.dirname(__file__),'b3.png'))
    b3_img = CTkImage(dark_image=b3, size=(390, 242))
    B3 = CTkButton(fr2, text='', font=('open sans', 30), width=200, height=251, corner_radius=0,
                   image=b3_img, border_width=0, fg_color='#1E1F22', hover_color='#EB6A00',
                   cursor='hand2', command=but3)
    B3.grid(row=1, column=0)
    b4 = Image.open(os.path.join(os.path.dirname(__file__),'b4.png'))
    b4_img = CTkImage(dark_image=b4, size=(390, 242))
    B4 = CTkButton(fr2, text='', font=('open sans', 30), width=200, height=251, corner_radius=0,
                   image=b4_img, border_width=0, fg_color='#1E1F22', hover_color='#EB6A00',
                   cursor='hand2', command=but4)
    B4.grid(row=1, column=1)
    back_but = CTkButton(fr2, text='< Back', font=('open sans', 20, 'bold'), bg_color='#1E1F22', fg_color='#1E1F22'
                         , hover_color='#1E1F22', corner_radius=0, command=Back, text_color='#EB6A00')
    back_but.place(x=4, y=4)

# ------main page pack button method-----------
def Back():
    fr2.destroy()
    plans.configure(state='normal')

bg = Image.open(os.path.join(os.path.dirname(__file__),'bg.png'))
bg1 = CTkImage(dark_image=bg, size=(800, 500))
bg_label = CTkLabel(window, image=bg1, text='')
bg_label.pack()
# -----------fr1-----------------
fr1 = CTkFrame(window, width=240, height=300, fg_color='#1E1F22', bg_color='#1E1F22')
fr1.place(x=300, y=100)
fr1.pack_propagate(False)
# ----------entryboxes------------
# weight = CTkEntry(fr1, width=210, font=('open sans', 20), placeholder_text='Enter your weight(kg)')
# weight.pack(padx=10, pady=10)
# height = CTkEntry(fr1, width=210, font=('open sans', 20), placeholder_text='Enter your height(cm)')
# height.pack(padx=10, pady=10)
# # ------------button----------------
# submit = CTkButton(fr1, text='Submit', font=('open sans', 15),
#                    fg_color='#EB6A00', hover_color='#B45609', command=BMI)
# submit.pack(padx=10, pady=10)
plans = CTkButton(fr1, text='chick here for workout plans >>', font=('open sans', 15),
                  fg_color='#EB6A00', hover_color='#1E1F22', cursor='hand2', command=Plans)
plans.pack(padx=10, pady=100)
# -------------Label---------------
L1 = CTkLabel(fr1, text='', font=('open sans', 20))
L1.pack()
L2 = CTkLabel(fr1, text='', font=('open sans', 20))
L2.pack()
window.mainloop()
