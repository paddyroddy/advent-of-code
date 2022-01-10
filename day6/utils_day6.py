import numpy as np


def _find_indices_which_changed(
    old_fish_timers: np.ndarray, new_fish_timers: np.ndarray
) -> list[int]:
    """
    in the event that the fish timer value is 0 need to compute
    which indices actually changed including new fish
    """
    n_old = len(old_fish_timers)
    n_new = len(new_fish_timers)
    changed_indices = list(np.where(old_fish_timers != new_fish_timers[:n_old])[0])
    new_indices = [] if n_new == n_old else list(range(n_old, n_new))
    return changed_indices + new_indices


def _handle_zero_timer(fish_timers: np.ndarray) -> np.ndarray:
    """
    fish with a 0 timer will be replaced by a new fish with a timer of 8
    """
    timer_zero = np.where(fish_timers == 0)[0]
    fish_timers[timer_zero] = 6
    new_fish = np.array([8] * len(timer_zero), dtype=int)
    return np.append(fish_timers, new_fish)


def _decrement_fish_timers(
    fish_timers: np.ndarray, fish_which_changed: list[int]
) -> np.ndarray:
    """
    decrement the timers of the rest of the fish
    """
    # add one to the fish which changed
    fish_timers[fish_which_changed] += 1
    fish_timers -= 1
    return fish_timers


def increment_day(fish_timers: np.ndarray) -> np.ndarray:
    """
    after a day has passed adjust all internal timers
    accordingly, a fish with a 0 initial state will become
    6 and produce a new fish with an internal timer of 8
    """
    new_fish_timers = _handle_zero_timer(fish_timers.copy())
    changed_indices = _find_indices_which_changed(fish_timers, new_fish_timers)
    return _decrement_fish_timers(new_fish_timers, changed_indices)


def compute_number_of_fish(fish_timers: np.ndarray) -> int:
    """
    compute the number of fish in the list of timers
    """
    return len(fish_timers)
