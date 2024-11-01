class BowlingGameV1:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        self.frames.append(pins)

    def score(self):
        total = 0
        new_frame = True
        current_frame = 1
        for i, pins in enumerate(self.frames):
            if current_frame > 10:
                break

            total += pins

            # It is a strike
            if pins == 10:
                # We make sure there are rolls
                if len(self.frames) > (i + 1):
                    total += self.frames[i + 1]
                # We make sure there are rolls
                if len(self.frames) > (i + 2):
                    total += self.frames[i + 2]

                new_frame = True
                current_frame += 1
            else:
                # spares can only happen with the second roll
                if not new_frame:
                    if pins + self.frames[i - 1] == 10:
                        if len(self.frames) > (i + 1):
                            total += self.frames[i + 1]

                new_frame = not new_frame
                if new_frame:
                    current_frame += 1

        return total
