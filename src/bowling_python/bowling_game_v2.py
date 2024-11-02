class Frame:
    def __init__(self, pins_first_roll):
        self.is_second_roll = False
        self.pins_first_roll = pins_first_roll
        self.pins_second_roll = 0
        self.second_roll_recorded = False
        self.bonus_roll = []

    def score_second_roll(self, pins):
        self.pins_second_roll = pins
        self.second_roll_recorded = True

    @property
    def is_strike_frame(self):
        return self.pins_first_roll == 10

    @property
    def is_spare_frame(self):
        return (
            not self.is_strike_frame
            and self.pins_first_roll + self.pins_second_roll == 10
        )

    def add_bonus_roll(self, pins):
        self.bonus_roll.append(pins)

    @property
    def score(self):
        bonus_score = 0
        for bonus in self.bonus_roll:
            bonus_score += bonus
        return self.pins_first_roll + self.pins_second_roll + bonus_score

    @property
    def is_completed_frame(self):
        return self.is_strike_frame or self.second_roll_recorded


class BowlingGameV2:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        if len(self.frames) == 10 and self.frames[-1].is_completed_frame:
            self.frames[-1].add_bonus_roll(pins)
            if self.frames[-2].is_strike_frame:
                if len(self.frames[-2].bonus_roll) < 2:
                    self.frames[-2].add_bonus_roll(pins)
            return

        if len(self.frames) > 0:
            if self.frames[-1].is_completed_frame:
                self.frames.append(Frame(pins))
            else:
                self.frames[-1].score_second_roll(pins)
        else:
            self.frames.append(Frame(pins))

        # We need to add bonus rolls
        self._add_spare_bonus_roll(pins)

        # For strikes, we need to check the two previous last rolls
        self._add_strike_bonus_roll(1, pins)
        self._add_strike_bonus_roll(2, pins)

    def _add_spare_bonus_roll(self, pins):
        # For spares, first, there needs to be a Frame
        # second needs to be the first roll of the current_frame
        # as spare can have only one bonus roll
        if len(self.frames) > 1:
            if not self.frames[-1].second_roll_recorded:
                if self.frames[-2].is_spare_frame:
                    self.frames[-2].add_bonus_roll(pins)

    def _add_strike_bonus_roll(self, frame, pins):
        if len(self.frames) > frame:
            if self.frames[-1 - frame].is_strike_frame:
                if len(self.frames[-1 - frame].bonus_roll) < 2:
                    self.frames[-1 - frame].add_bonus_roll(pins)

    def score(self):
        total = 0
        for frame in self.frames:
            total += frame.score

        return total
