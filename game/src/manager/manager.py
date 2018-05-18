import Assets

class Manager(object):
    """docstring for Manager"""

    def __init__(self, core):
        super(Manager, self).__init__()
        self.Core = core

        self.Assets = assets.Assets()

        self.state_stack = []

    def run(self):

        self.Core.Window.make_screen()

        while True:

            curr_state = len(self.state_stack)

            # if state_stack in last position is running:
            if self.state_stack[curr_state].get_is_running():
                self.state_stack[curr_state].run()  # Run it!

            # Not running, huh? It is paused? If so, Resume:
            elif state_stack[curr_state].get_is_paused():
                state_stack[curr_state].resume()

            else:  # Not running nor paused?
                # This function should return a state
                aux_state = self.state_stack[cur_state].get_next_state()
                # This should return False or a State.

                if aux_state:
                    # This function pauses currente state's logic.
                    self.state_stack[curr_state].pause()

                    # Then appends the new state returned by the current state to the stack
                    self.state_stack.append(aux_state)

                elif not curr_state == 0:  # If isnt Title_screen
                    # State that was before
                    # Sometimes you'll need values from the next state.
                    self.state_stack[cur_state - 1].recieve_arg(self.state_stack[curr_state].get_arg())
                    # Delete's Class from memory
                    self.state_stack[curr_state].close()
                    self.state_stack.pop()                          # Remove it from the Stack

            self.Core.Window.update_screen()
