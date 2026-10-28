from pico2d import load_image, get_time, SDL_KEYDOWN
from transitions import Machine
import math


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
        self.wait_start_time = get_time()

        # IDLE과 SLEEP 상태를 정의한다.
        self.machine = Machine(
            model=self,
            states=['IDLE', 'SLEEP'],
            initial='IDLE',
            auto_transitions=False,
        )

        # 상태 전이 규칙 설정
        self.machine.add_transition(
            trigger='time_out',
            source='IDLE',
            dest='SLEEP',
        )
        self.machine.add_transition(
            trigger='key_down',
            source='SLEEP',
            dest='IDLE',
        )

    def on_enter_IDLE(self):
        self.wait_start_time = get_time()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if self.state == 'SLEEP':
                self.key_down()

    def update(self):
        if self.state == 'IDLE':
            self.frame = (self.frame + 1) % 8
            if get_time() - self.wait_start_time > 5.0:
                self.time_out()
        elif self.state == 'SLEEP':
            self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.state == 'IDLE':
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.state == 'SLEEP':
            if self.face_dir == 1:
                self.image.clip_composite_draw(
                    self.frame * 100, 300, 100, 100,
                    math.pi / 2, '', self.x - 25, self.y - 25, 100, 100
                )
            else:
                self.image.clip_composite_draw(
                    self.frame * 100, 200, 100, 100,
                    -math.pi / 2, '', self.x + 25, self.y - 25, 100, 100
                )
