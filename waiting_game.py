# tell the user the target time is 4 seconds
# ---Press Enter to begin ---
# ...Press Enter again after 4 seconds...
# tell player if too fast/slow or right on
# Elapsed time: 4.213 seconds
# (0.213 seconds too slow)
def waiting_game():
    """The aim is to stop at 4 seconds exactly"""
    INTRO = """This is the waiting game \n,
            The target is to stop the timer at 4 second \n
            The timer starts and stops when you press enter
            """
    TARGET = float(4.000)
    result = float
    def Enter_key_input():
        """Doc String"""

        def start_pressed():
            """Doc String"""
            pass

        def stop_pressed():
            """Doc String"""
            pass

        def show_result(self, result):
            """Too Fast!, Too Slow, We have a winner!"""
            under = float
            # Too Fast
            if result<self.TARGET:
                 under = self.TARGET - self.result
                return "Elapsed time: ", self.result, "Too Fast by ", under


            # Too Slow
            elif result > self.TARGET:
                over = float
                over = (float(self.TARGET - self.result))

            def time_elapsed():
                """Doc String"""
                pass


