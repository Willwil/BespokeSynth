#use with Kontakt 5

def on_pulse():
   step = bespoke.get_step(16)
   if step % 8 == 0:
      this.play_note(45, 65, 1.0/16)
   if step % 8 == 4:
      this.play_note(45, 70, 1.0/16)
   if step % 16 == 15 and bespoke.get_measure() % 4 == 3:
      this.play_note(45, 65, 1.0/16)
   if step % 8 == 4:
      this.play_note(42, 127, 1.0/16)
      if random.random() < .3:
         this.schedule_note(1.0/16,42,100,1.0/16)
      if random.random() < .3:
         this.schedule_note(1.0/8,42,100,1.0/16)
   if random.random() < .7:
      this.play_note(random.choice([57,71]), 96, 1.0/16)
   v = get_hat_velocity()
   this.play_note(44, v, 1.0/16)
      
def get_hat_velocity():
   velocities = [40,80,120,50]
   ret = velocities[(bespoke.get_step(16) % 32) % len(velocities)]
   this.output(str(ret))
   return ret 