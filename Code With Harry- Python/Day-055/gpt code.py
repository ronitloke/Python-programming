from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, Tuple


class Move(str, Enum):
    SNAKE = "snake"
    WATER = "water"
    GUN = "gun"

    @classmethod
    def parse(cls, raw: str) -> "Move":
        cleaned = raw.strip().lower()
        try:
            return cls(cleaned)
        except ValueError as e:
            allowed = ", ".join(m.value for m in cls)
            raise ValueError(f"Invalid move: '{raw}'. Allowed: {allowed}") from e


class Outcome(str, Enum):
    COMP_WINS = "Comp wins"
    PLAYER_WINS = "Player wins"
    DRAW = "Draw"


@dataclass(frozen=True)
class Rules:
    # winner_map[winner] = set(of losers)
    winner_map: Dict[Move, FrozenSet[Move]]

    def outcome(self, comp: Move, player: Move) -> Outcome:
        if comp == player:
            return Outcome.DRAW
        if comp in self.winner_map[player]:
            return Outcome.PLAYER_WINS
        if player in self.winner_map[comp]:
            return Outcome.COMP_WINS
        raise RuntimeError("Rules are inconsistent / incomplete.")


DEFAULT_RULES = Rules(
    winner_map={
        Move.SNAKE: frozenset({Move.WATER}),
        Move.WATER: frozenset({Move.GUN}),
        Move.GUN: frozenset({Move.SNAKE}),
    }
)


@dataclass
class Score:
    player: int = 0
    comp: int = 0
    draws: int = 0


def prompt_move(prompt: str = "Your move (snake/water/gun): ") -> Move:
    while True:
        try:
            return Move.parse(input(prompt))
        except ValueError as err:
            print(err)


def comp_move(rng: random.Random) -> Move:
    return rng.choice(list(Move))


def play_round(rules: Rules, rng: random.Random) -> Tuple[Move, Move, Outcome]:
    player = prompt_move()
    comp = comp_move(rng)
    result = rules.outcome(comp=comp, player=player)
    return comp, player, result


def update_score(score: Score, outcome: Outcome) -> None:
    if outcome == Outcome.PLAYER_WINS:
        score.player += 1
    elif outcome == Outcome.COMP_WINS:
        score.comp += 1
    else:
        score.draws += 1


def is_match_over(score: Score, best_of: int) -> bool:
    wins_needed = best_of // 2 + 1
    return score.player >= wins_needed or score.comp >= wins_needed


def main(best_of: int = 5, seed: int | None = None) -> None:
    if best_of <= 0 or best_of % 2 == 0:
        raise ValueError("best_of must be a positive odd number (e.g., 3, 5, 7).")

    rng = random.Random(seed)
    rules = DEFAULT_RULES
    score = Score()

    print(f"Snake-Water-Gun | Best of {best_of}")
    print("Type: snake / water / gun (any case is fine)")

    round_no = 1
    while not is_match_over(score, best_of):
        comp, player, outcome = play_round(rules, rng)

        print(f"\nRound {round_no}")
        print(f"Comp   : {comp.value}")
        print(f"Player : {player.value}")
        print(f"Result : {outcome.value}")

        update_score(score, outcome)
        print(f"Score  : Player {score.player} | Comp {score.comp} | Draws {score.draws}")

        round_no += 1

    winner = "PLAYER" if score.player > score.comp else "COMP"
    print(f"\nMatch Over ✅ Winner: {winner}")


if __name__ == "__main__":
    main(best_of=5, seed=None)